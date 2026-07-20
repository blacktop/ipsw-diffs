## CoreFoundation

> `/System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__dof_NSAppNap`
- `__TEXT.__dof_CFRunLoop`
- `__TEXT.__dof_Cocoa_Aut`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_nlclslist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_nlcatlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__const_cfobj2`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-5027.0.59.0.0
-  __TEXT.__text: 0x2074c4
+5027.0.63.2.0
+  __TEXT.__text: 0x2077b4
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x8434
   __TEXT.__const: 0x1a8114
-  __TEXT.__oslogstring: 0xb2ea
-  __TEXT.__cstring: 0xbbaf0
-  __TEXT.__gcc_except_tab: 0x6864
+  __TEXT.__oslogstring: 0xb313
+  __TEXT.__cstring: 0xbbb36
+  __TEXT.__gcc_except_tab: 0x6848
   __TEXT.__ustring: 0x1446
   __TEXT.__dlopen_cstrs: 0xcc
   __TEXT.__dof_NSAppNap: 0x4cf

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3ac730
+  __DATA_CONST.__const: 0x3ac740
   __DATA_CONST.__objc_classlist: 0x4c0
   __DATA_CONST.__objc_nlclslist: 0x58
   __DATA_CONST.__objc_catlist: 0x18

   __DATA_CONST.__got: 0x540
   __AUTH_CONST.__const: 0x93a0
   __AUTH_CONST.__cfstring: 0xd55a0
-  __AUTH_CONST.__objc_const: 0xb1e8
+  __AUTH_CONST.__objc_const: 0xb208
   __AUTH_CONST.__const_cfobj2: 0x40
   __AUTH_CONST.__objc_dictobj: 0x848
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0x19e8
   __AUTH.__objc_data: 0xcd0
   __AUTH.__data: 0x120
-  __DATA.__objc_ivar: 0x66c
+  __DATA.__objc_ivar: 0x670
   __DATA.__data: 0x94d
   __DATA.__cf_except_bt: 0x2000
   __DATA.__cf_except_pack: 0x410
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x1070
+  __DATA.__bss: 0x1050
   __DATA.__common: 0xc0
   __DATA_DIRTY.__objc_data: 0x22b0
   __DATA_DIRTY.__data: 0x198
-  __DATA_DIRTY.__bss: 0xcc8
+  __DATA_DIRTY.__bss: 0xce8
   __DATA_DIRTY.__common: 0x3e8
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/CoreServicesInternal.framework/Versions/A/CoreServicesInternal

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/liboah.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9403
-  Symbols:   14831
-  CStrings:  31427
+  Functions: 9406
+  Symbols:   14835
+  CStrings:  31431
 
Symbols:
+ -[CFPrefsDaemon createQueueForClientWithPID:uid:]
+ -[CFPrefsDaemon createSecondaryQueueForClientWithPID:]
+ -[CFPrefsDaemon listenerWorkloopForRoleAccountUID:]
+ GCC_except_table125
+ GCC_except_table287
+ OBJC_IVAR_$_CFPrefsDaemon._roleAccountsListenerWorkloops
+ _CFPreferencesManagementStatusChangedForDomains
+ _CFPreferencesPostValuesChangedInDomains
- -[CFPrefsDaemon createQueueForClientWithPID:secondary:]
- GCC_except_table288
- GCC_except_table96
- _handleExternalNotification
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZKMyIm/Sources/CoreFoundation/CoreFoundation/PlugIn.subproj/CFBundle.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZKMyIm/Sources/CoreFoundation/CoreFoundation/PlugIn.subproj/CFBundle_Binary.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZKMyIm/Sources/CoreFoundation/CoreFoundation/PlugIn.subproj/CFBundle_Executable.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZKMyIm/Sources/CoreFoundation/CoreFoundation/PlugIn.subproj/CFBundle_InfoPlist.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZKMyIm/Sources/CoreFoundation/CoreFoundation/PlugIn.subproj/CFBundle_Locale.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZKMyIm/Sources/CoreFoundation/CoreFoundation/PlugIn.subproj/CFBundle_Main.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZKMyIm/Sources/CoreFoundation/CoreFoundation/PlugIn.subproj/CFBundle_Resources.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZKMyIm/Sources/CoreFoundation/CoreFoundation/PlugIn.subproj/CFBundle_Strings.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ZKMyIm/Sources/CoreFoundation/CoreFoundation/PlugIn.subproj/CFPlugIn.c"
+ "/usr/bin/security"
+ "/usr/libexec/lsd"
+ "com.apple.cfprefsd.incoming.uid-%u"
+ "proc_pidpath(%i) error: %{darwin.errno}d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GnLlNo/Sources/CoreFoundation/CoreFoundation/PlugIn.subproj/CFBundle.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GnLlNo/Sources/CoreFoundation/CoreFoundation/PlugIn.subproj/CFBundle_Binary.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GnLlNo/Sources/CoreFoundation/CoreFoundation/PlugIn.subproj/CFBundle_Executable.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GnLlNo/Sources/CoreFoundation/CoreFoundation/PlugIn.subproj/CFBundle_InfoPlist.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GnLlNo/Sources/CoreFoundation/CoreFoundation/PlugIn.subproj/CFBundle_Locale.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GnLlNo/Sources/CoreFoundation/CoreFoundation/PlugIn.subproj/CFBundle_Main.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GnLlNo/Sources/CoreFoundation/CoreFoundation/PlugIn.subproj/CFBundle_Resources.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GnLlNo/Sources/CoreFoundation/CoreFoundation/PlugIn.subproj/CFBundle_Strings.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GnLlNo/Sources/CoreFoundation/CoreFoundation/PlugIn.subproj/CFPlugIn.c"
```
