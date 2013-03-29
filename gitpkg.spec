# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       gitpkg

# >> macros
# << macros

Summary:    Helps manage packaging in git
Version:    0.0.3
Release:    1
Group:      Development
License:    GPLv2
Source0:    gitpkg-0.0.1.tar.bz2
Source100:  gitpkg.yaml
Requires:   git
Requires:   pristine-tar
Requires:   python
BuildRequires:  python

%description
Allows the packaging to be maintained in a discrete git tree in the same git repo as the source


%prep
%setup -q -n src

# >> setup
# << setup

%build
# >> build pre
# << build pre


make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post


%files
%defattr(-,root,root,-)
%{_bindir}/gp_release
%{_bindir}/gp_setup
%{_bindir}/gp_mkpkg
%{_datadir}/gitpkg/gp_common
%{_libdir}/obs/service/gitpkg
%{_libdir}/obs/service/gitpkg.service
%{_libdir}/obs/service/gp_mkpkg
%{_libdir}/python2.7/site-packages/BlockDumper.py
%{_libdir}/python2.7/site-packages/BlockDumper.pyc
%{_libdir}/python2.7/site-packages/BlockDumper.pyo
%{_libdir}/python2.7/site-packages/gitpkg-0.0.2-py2.7.egg-info
# >> files
# << files