%define upstream_name    RT-Client-Console
%define upstream_version 0.2.0

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Non-blocking Curses.pm input for full-screen console apps
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/RT/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Config::Tiny)
BuildRequires: perl(Curses)
BuildRequires: perl(Curses::Forms)
BuildRequires: perl(Curses::Widgets)
BuildRequires: perl(Error)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(POE)
BuildRequires: perl(Params::Validate)
BuildRequires: perl(RT::Client::REST)
BuildRequires: perl(Test::More)
BuildRequires: perl(parent)
BuildRequires: perl(relative)
BuildRequires: perl(version)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
RT::Client::Console distribution provides an executable _rtconsole_ and
modules. The executable is a full-featured curses-based interface to any RT
server that has REST interface enabled.

The modules provides comprehensive ways to connect, interact and display
informations from the RT server. A plugin mechanism is planned, and will
enable more flexibility.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README META.yml
%{_bindir}/*
%{_mandir}/man?/*
%perl_vendorlib/*
