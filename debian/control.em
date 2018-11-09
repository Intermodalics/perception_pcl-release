Source: @(Package)
Section: misc
Priority: extra
Maintainer: @(Maintainer)
Build-Depends: debhelper (>= @(debhelper_version).0.0), libpcl-dev (>= 1.8), @(', '.join(BuildDepends))
Homepage: @(Homepage)
Standards-Version: 3.9.2

Package: @(Package)-pcl-1.8
Provides: @(Package)
Conflicts: @(Package)
Replaces: @(Package)
Architecture: any
Depends: ${shlibs:Depends}, ${misc:Depends}, libpcl-dev (>= 1.8), @(', '.join(Depends))
@[if Conflicts]Conflicts: @(', '.join(Conflicts))@\n@[end if]@
@[if Replaces]Replaces: @(', '.join(Replaces))@\n@[end if]@
Description: @(Description)
