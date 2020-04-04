%{?scl:%scl_package perl-Filter-Simple}

%global base_version 0.94
Name:           %{?scl_prefix}perl-Filter-Simple
Version:        0.95
Release:        451%{?dist}
Summary:        Simplified Perl source filtering
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Filter-Simple
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Filter-Simple-%{base_version}.tar.gz
BuildArch:      noarch
# Unbundled from perl 5.28.0-RC1
Patch0:         Filter-Simple-0.94-Upgrade-to-0.95.patch
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  %{?scl_prefix}perl(strict)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Filter::Util::Call)
BuildRequires:  %{?scl_prefix}perl(Text::Balanced) >= 1.97
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Tests:
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(parent)
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Text::Balanced) >= 1.97
Requires:       %{?scl_prefix}perl(warnings)

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(Text::Balanced\\)$

%description
The Filter::Simple Perl module provides a simplified interface to
Filter::Util::Call; one that is sufficient for most common cases.

%prep
%setup -q -n Filter-Simple-%{base_version}
%patch0 -p1

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Dec 20 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.95-451
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-439
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.95-438
- Increase release to favour standalone package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-417
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.95-416
- Increase release to favour standalone package

* Thu May 24 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.95-1
- Upgrade to 0.95 as provided in perl-5.28.0-RC1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 10 2017 Petr Pisar <ppisar@redhat.com> - 0.94-1
- 0.94 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.93-394
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.93-393
- Perl 5.26 rebuild

* Thu May 11 2017 Petr Pisar <ppisar@redhat.com> - 0.93-1
- Upgrade to 0.93 as provided in perl-5.25.12

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-366
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.92-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.92-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.92-346
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.92-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.92-2
- Perl 5.22 rebuild

* Wed May 06 2015 Petr Pisar <ppisar@redhat.com> - 0.92-1
- 0.92 bump in order to dual-live with perl 5.22

* Tue Nov 18 2014 Petr Pisar <ppisar@redhat.com> - 0.91-340
- Increase release number to supersede perl's sub-package

* Wed Oct 29 2014 Petr Pisar <ppisar@redhat.com> 0.91-240
- Specfile autogenerated by cpanspec 1.78.
