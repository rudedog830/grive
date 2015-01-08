#Correct it to 1 if you want git snapshot version
Name:           grive
Version:        0.3.0
Release:        1%{?dist}

Summary:        An open source Linux client for Google Drive

License:        GPLv2
URL:            http://grive.github.com/grive/
Source:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  libstdc++-devel
BuildRequires:  libcurl-devel
BuildRequires:  json-c-devel
BuildRequires:  expat-devel
BuildRequires:  openssl-devel
BuildRequires:  boost-devel

%description
The purpose of this project is to provide an independent implementation
of Google Drive client. It uses the Google Document List API to talk to
the servers in Google. The code is written in standard C++.


%package        devel
Summary:        Development files for grive
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for grive

%prep
%setup -q -n grive


%build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr .
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc COPYING README
%_mandir/man1/%{name}.1.gz
%{_bindir}/%{name}
%{_bindir}/b%{name}
