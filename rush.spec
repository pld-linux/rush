Summary:	restricted user shell
Summary(pl.UTF-8):	powłoka z ograniczeniami
Name:		rush
Version:	1.7
Release:	1
License:	GPL v3+
Group:		Applications/Shells
Source0:	http://ftp.gnu.org/gnu/rush/%{name}-%{version}.tar.gz
# Source0-md5:	01c42be5359d2c31e2145eb112cd94cf
URL:		http://www.gnu.org/software/rush/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Rush is a Restricted User Shell, designed for sites providing
limited remote access to their resources, such as, for example,
savannah.gnu.org. Its main program, rush, is configured as a user
login shell for users that are allowed only remote access to the
machine. Using a flexible configuration file, GNU Rush gives
administrator complete control over the command lines that users
execute, and allows to tune the usage of system resources, such as
virtual memory, CPU time, etc. on a per-user basis.

%description -l pl.UTF-8
GNU Rush to ograniczona powłoka użytkownika, zaprojektowana dla
systemów udostępnijących ograniczony dostęp do zasobów, jak np.
savannah.gnu.org. Główny program, rush, jest ustawiony jako domyślna
powłoka dla użytkowników mających tylko zdalny dostep do maszyny. Za
pomocą elastycznego pliku konfiguracyjnego, GNU Rush pozwala
administratorowi na kompletną kontrolę nad poleceniami wywoływanymi
przez użytkownika oraz pozwala na okreslenie limitów zasobów, takich
jak pamięć wirtualna, czas pracy procesora, itp.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rush.rc
%{_infodir}/rush.info*
%{_datadir}/rush
