#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define	pnam	Application-Plugin-TT
Summary:	CGI::Application::Plugin::TT - Add Template Toolkit support to CGI::Application
#Summary(pl.UTF-8):	
Name:		perl-CGI-Application-Plugin-TT
Version:	1.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CGI/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d1b22bd5873911087ceb5d2c48311326
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/CGI-Application-Plugin-TT/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-CGI-Application >= 4.0
BuildRequires:	perl-Template-Toolkit >= 2.0
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Application::Plugin::TT adds support for the popular Template Toolkit engine
to your CGI::Application modules by providing several helper methods that
allow you to process template files from within your runmodes.

It compliments the support for HTML::Template that is built into CGI::Application
through the load_tmpl method.  It also provides a few extra features than just the ability
to load a template.



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/CGI/Application/Plugin/*.pm
#%{perl_vendorlib}/CGI/Application/Plugin/TT
%{_mandir}/man3/*
