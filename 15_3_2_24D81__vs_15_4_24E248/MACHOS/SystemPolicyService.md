## SystemPolicyService

> `/System/Library/PrivateFrameworks/ConfigurationProfiles.framework/XPCServices/SystemPolicyService.xpc/Contents/MacOS/SystemPolicyService`

```diff

-1851.2.2.0.0
-  __TEXT.__text: 0xc2fc
+1851.4.12.0.0
+  __TEXT.__text: 0xc304
   __TEXT.__auth_stubs: 0x760
-  __TEXT.__objc_stubs: 0xec0
-  __TEXT.__objc_methlist: 0x50
-  __TEXT.__gcc_except_tab: 0x13c8
-  __TEXT.__cstring: 0x22ed
-  __TEXT.__objc_methname: 0xb01
+  __TEXT.__objc_stubs: 0xea0
+  __TEXT.__objc_methlist: 0xa0
+  __TEXT.__gcc_except_tab: 0x13b8
+  __TEXT.__cstring: 0x22fc
+  __TEXT.__objc_methname: 0xae0
   __TEXT.__objc_classname: 0x68
   __TEXT.__objc_methtype: 0xcd
   __TEXT.__const: 0x48
   __TEXT.__oslogstring: 0xe
-  __TEXT.__unwind_info: 0x588
+  __TEXT.__unwind_info: 0x598
   __DATA_CONST.__auth_got: 0x3c8
   __DATA_CONST.__got: 0x288
   __DATA_CONST.__const: 0x530
-  __DATA_CONST.__cfstring: 0x24a0
+  __DATA_CONST.__cfstring: 0x24c0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_arraydata: 0x190
+  __DATA_CONST.__objc_arraydata: 0x198
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0xa8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x140
+  __DATA.__objc_const: 0xc8
   __DATA.__objc_selrefs: 0x3e8
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x178

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7A2EF60D-9B05-3D62-88F5-2CA90B127D57
-  Functions: 218
+  UUID: 21CE9A01-2E8F-3D10-A50F-30258CE27F0A
+  Functions: 237
   Symbols:   214
-  CStrings:  763
+  CStrings:  764
 
CStrings:
+ "++Enabled sudden term (%@:%@): %@"
+ "--Disabled sudden term (%@:%@): %@"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools/Common/CFUtil.cp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools/Common/CertificateInfo.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools/Common/LocUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools/Common/Logger.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools/Common/MiscUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools/Common/NSUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools/Common/ODUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools/Common/StdErrors.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools/Common/SuddenTermUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools/Common/XPCUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools/ConfigProfiles/CPCommon/CPDestination.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools/ConfigProfiles/CPCommon/ConfigProfileUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools/ConfigProfiles/CPCommon/MDMXPCUtil.mm"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/MCXTools/ConfigProfiles/CPServices/SystemPolicy/SystemPolicyService.mm"
+ "Factory"
+ "IsRunningAsDaemon:bootstrap_parent failed: %d"
- "++Enabled sudden term (%@:%@:%@): %@"
- "--Disabled sudden term (%@:%@:%@): %@"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools/Common/CFUtil.cp"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools/Common/CertificateInfo.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools/Common/LocUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools/Common/Logger.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools/Common/MiscUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools/Common/NSUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools/Common/ODUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools/Common/StdErrors.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools/Common/SuddenTermUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools/Common/XPCUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools/ConfigProfiles/CPCommon/CPDestination.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools/ConfigProfiles/CPCommon/ConfigProfileUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools/ConfigProfiles/CPCommon/MDMXPCUtil.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/MCXTools/ConfigProfiles/CPServices/SystemPolicy/SystemPolicyService.mm"
- "Unknown Malware Upload State: %@"
- "_suddenTerminationDisablingCount"

```
