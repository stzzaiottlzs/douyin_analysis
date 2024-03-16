# 从官方 Python 基础镜像开始
FROM centos:7

# 将当前工作目录设置为 /code
# 这是放置 requirements.txt 文件和应用程序目录的地方
WORKDIR /root

RUN mkdir douyin_analysis

# 复制 requirements.txt 文件
# 由于这个文件不经常更改，Docker 会检测它并在这一步使用缓存，也为下一步启用缓存
COPY ./requirements.txt /root/requirements.txt

COPY ./google_chrome.repo /etc/yum.repos.d/

RUN yum install -y google-chrome-stable
RUN yum install -y gcc
RUN yum install -y make
RUN yum -y groupinstall "Development tools"
RUN yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
RUN yum install libffi-devel -y
RUN yum install perl-IPC-Cmd -y
#RUN yum install -y python3.11
COPY ./openssl-1.1.1w.tar.gz /root/openssl-1.1.1w.tar.gz
COPY ./Python-3.11.7.tgz /root/Python-3.11.7.tgz
RUN tar -zxvf /root/openssl-1.1.1w.tar.gz
RUN cd /root/openssl-1.1.1w; ./config --prefix=/usr/local/openssl; make && make install
#RUN mv /usr/bin/openssl /usr/bin/openssl.old
#RUN mv /usr/lib64/openssl /usr/lib64/openssl.old
RUN mv /usr/lib64/libssl.so /usr/lib64/libssl.so.old
RUN ln -s /usr/local/openssl/bin/openssl /usr/bin/openssl
RUN ln -s /usr/local/openssl/include/openssl /usr/include/openssl
RUN ln -s /usr/local/openssl/lib/libssl.so /usr/lib64/libssl.so
RUN echo "/usr/local/openssl/lib" >> /etc/ld.so.conf
RUN ldconfig -v

RUN openssl version

RUN tar -zxvf /root/Python-3.11.7.tgz
RUN cd /root/Python-3.11.7;./configure --prefix=/usr/local/python3 --with-openssl=/usr/local/openssl;make && make install
RUN ln -s /usr/local/python3/bin/python3 /usr/bin/python3
RUN ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3

# 运行 pip 命令安装依赖项
RUN pip3 install --no-cache-dir --upgrade -r /root/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 复制 FastAPI 项目代码
COPY ./CODES /root/douyin_analysis/CODES

EXPOSE 8080

# 运行服务
CMD ["python3", "/root/douyin_analysis/CODES/main.py"]

