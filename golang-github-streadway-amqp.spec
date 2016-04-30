Name     : golang-github-streadway-amqp
Version  : 0
Release  : 5
URL      : https://github.com/streadway/amqp/archive/79beb307dcf5904fb8cb061276f1c14f222012c2.tar.gz
Source0  : https://github.com/streadway/amqp/archive/79beb307dcf5904fb8cb061276f1c14f222012c2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
BuildRequires: go

%description
# AMQP
AMQP 0.9.1 client with RabbitMQ extensions in Go.
# Status
*Beta*
[![Build Status](https://secure.travis-ci.org/streadway/amqp.png)](http://travis-ci.org/streadway/amqp)

%prep
%setup -q -n amqp-79beb307dcf5904fb8cb061276f1c14f222012c2

%build

%install
%global gopath /usr/lib/golang
%global library_path github.com/streadway/amqp
rm -rf %{buildroot}
install -d -p %{buildroot}%{gopath}/src/%{library_path}/
for file in $(find . -iname "*.go") ; do
     install -d -p %{buildroot}%{gopath}/src/%{library_path}/$(dirname $file)
     cp -pav $file %{buildroot}%{gopath}/src/%{library_path}/$file
done

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export GOPATH=%{buildroot}%{gopath}
go test %{library_path}

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/streadway/amqp/_examples/pubsub/pubsub.go
/usr/lib/golang/src/github.com/streadway/amqp/_examples/simple-consumer/consumer.go
/usr/lib/golang/src/github.com/streadway/amqp/_examples/simple-producer/producer.go
/usr/lib/golang/src/github.com/streadway/amqp/allocator.go
/usr/lib/golang/src/github.com/streadway/amqp/allocator_test.go
/usr/lib/golang/src/github.com/streadway/amqp/auth.go
/usr/lib/golang/src/github.com/streadway/amqp/channel.go
/usr/lib/golang/src/github.com/streadway/amqp/client_test.go
/usr/lib/golang/src/github.com/streadway/amqp/confirms.go
/usr/lib/golang/src/github.com/streadway/amqp/confirms_test.go
/usr/lib/golang/src/github.com/streadway/amqp/connection.go
/usr/lib/golang/src/github.com/streadway/amqp/consumers.go
/usr/lib/golang/src/github.com/streadway/amqp/delivery.go
/usr/lib/golang/src/github.com/streadway/amqp/delivery_test.go
/usr/lib/golang/src/github.com/streadway/amqp/doc.go
/usr/lib/golang/src/github.com/streadway/amqp/examples_test.go
/usr/lib/golang/src/github.com/streadway/amqp/fuzz.go
/usr/lib/golang/src/github.com/streadway/amqp/integration_test.go
/usr/lib/golang/src/github.com/streadway/amqp/read.go
/usr/lib/golang/src/github.com/streadway/amqp/read_test.go
/usr/lib/golang/src/github.com/streadway/amqp/reconnect_test.go
/usr/lib/golang/src/github.com/streadway/amqp/return.go
/usr/lib/golang/src/github.com/streadway/amqp/shared_test.go
/usr/lib/golang/src/github.com/streadway/amqp/spec/gen.go
/usr/lib/golang/src/github.com/streadway/amqp/spec091.go
/usr/lib/golang/src/github.com/streadway/amqp/tls_test.go
/usr/lib/golang/src/github.com/streadway/amqp/types.go
/usr/lib/golang/src/github.com/streadway/amqp/uri.go
/usr/lib/golang/src/github.com/streadway/amqp/uri_test.go
/usr/lib/golang/src/github.com/streadway/amqp/write.go
