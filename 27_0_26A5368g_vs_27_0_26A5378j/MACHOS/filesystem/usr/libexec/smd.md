## smd

> `/usr/libexec/smd`

```diff

-  __TEXT.__text: 0xffa4
-  __TEXT.__auth_stubs: 0xc40
-  __TEXT.__objc_stubs: 0x14a0
+  __TEXT.__text: 0x107b8
+  __TEXT.__auth_stubs: 0xc80
+  __TEXT.__objc_stubs: 0x1500
   __TEXT.__objc_methlist: 0x9f0
-  __TEXT.__const: 0x298
-  __TEXT.__oslogstring: 0x187a
+  __TEXT.__const: 0x2a0
+  __TEXT.__oslogstring: 0x192f
   __TEXT.__objc_classname: 0x1b1
-  __TEXT.__objc_methtype: 0xa74
-  __TEXT.__objc_methname: 0x147a
-  __TEXT.__cstring: 0x1244
+  __TEXT.__objc_methtype: 0xa85
+  __TEXT.__objc_methname: 0x14d1
+  __TEXT.__cstring: 0x134f
   __TEXT.__gcc_except_tab: 0x2dc
-  __TEXT.__unwind_info: 0x3c8
-  __DATA_CONST.__const: 0x4e8
-  __DATA_CONST.__cfstring: 0x80
+  __TEXT.__unwind_info: 0x3d0
+  __DATA_CONST.__const: 0x518
+  __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__auth_got: 0x630
-  __DATA_CONST.__got: 0x110
+  __DATA_CONST.__auth_got: 0x650
+  __DATA_CONST.__got: 0x130
   __DATA.__objc_const: 0xf70
-  __DATA.__objc_selrefs: 0x5f0
+  __DATA.__objc_selrefs: 0x608
   __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x2c0

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/AppServerSupport.framework/Versions/A/AppServerSupport
   - /System/Library/PrivateFrameworks/BackgroundTaskManagement.framework/Versions/A/BackgroundTaskManagement
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 276
-  Symbols:   240
-  CStrings:  689
+  Functions: 281
+  Symbols:   246
+  CStrings:  722
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_NSNumber
+ ___kCFBooleanTrue
+ _csops_audittoken
+ _fgetxattr
+ _strstr
CStrings:
+ "(none)"
+ "(unknown)"
+ ".app/"
+ ".appex/"
+ ".bundle/"
+ ".framework/"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.YpZto6/Binaries/libxpc_executables/install/Symbols/smd"
+ "@\"NSDictionary\"8@?0"
+ "@\"NSObject<OS_xpc_object>\"32@0:8r*16^I24"
+ "@(#)VERSION:Darwin Privileged Tool Bootstrapper Version 2.0.0: Tue Jun 30 21:11:48 PDT 2026; root:libxpc_executables-3298.0.10~59/smd/RELEASE_ARM64E"
+ "@32@0:8r*16^I24"
+ "@72@0:8q16r*24@32I40I44@48@56@64"
+ "@80@0:8q16r*24@32@40I48I52@56@64@72"
+ "Darwin Privileged Tool Bootstrapper Version 2.0.0: Tue Jun 30 21:11:48 PDT 2026; root:libxpc_executables-3298.0.10~59/smd/RELEASE_ARM64E"
+ "_Quarantined"
+ "binary_cdhash"
+ "binary_path"
+ "binary_team_id"
+ "caller_is_sandboxed"
+ "com.apple.libxpc.smd.platform_binary_caller"
+ "com.apple.quarantine"
+ "copyPlist:flagsOut:"
+ "dictionary"
+ "initWithType:path:container:plist:plist_flags:uid:domain:btm:launchd:"
+ "initWithType:path:plist:plist_flags:uid:domain:btm:launchd:"
+ "is_bundled"
+ "is_platform_binary"
+ "job_label"
+ "job_program"
+ "numberWithBool:"
+ "numberWithInt:"
+ "pid"
+ "setDefaultPlistProperties:plist_flags:type:"
+ "smjob_submit_observation: would-block exploit signature -- pid=%d is_platform_binary=%d is_bundled=%d path=%{public}s team_id=%{public}s job_label=%{public}s job_program=%{public}s"
+ "v36@0:8@16I24q28"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.SiUysI/Binaries/libxpc_executables/install/Symbols/smd"
- "@\"NSObject<OS_xpc_object>\"24@0:8r*16"
- "@(#)VERSION:Darwin Privileged Tool Bootstrapper Version 2.0.0: Sat Jun 13 22:21:56 PDT 2026; root:libxpc_executables-3298.0.4~137/smd/RELEASE_ARM64E"
- "@24@0:8r*16"
- "@68@0:8q16r*24@32I40@44@52@60"
- "@76@0:8q16r*24@32@40I48@52@60@68"
- "Darwin Privileged Tool Bootstrapper Version 2.0.0: Sat Jun 13 22:21:56 PDT 2026; root:libxpc_executables-3298.0.4~137/smd/RELEASE_ARM64E"
- "copyPlist:"
- "initWithType:path:container:plist:uid:domain:btm:launchd:"
- "initWithType:path:plist:uid:domain:btm:launchd:"
- "setDefaultPlistProperties:type:"
- "v32@0:8@16q24"

```
