## FamilyControlsAgent

> `/System/Library/Frameworks/FamilyControls.framework/FamilyControlsAgent`

```diff

-1223.100.15.0.0
-  __TEXT.__text: 0x5c900
-  __TEXT.__auth_stubs: 0x2080
+1223.100.16.0.0
+  __TEXT.__text: 0x5d744
+  __TEXT.__auth_stubs: 0x20a0
   __TEXT.__objc_stubs: 0x16c0
   __TEXT.__objc_methlist: 0x7ac
-  __TEXT.__const: 0x1ce8
-  __TEXT.__oslogstring: 0x32cb
-  __TEXT.__cstring: 0xa36
+  __TEXT.__const: 0x1cf8
+  __TEXT.__oslogstring: 0x34eb
+  __TEXT.__cstring: 0xa66
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0xc54
   __TEXT.__swift5_typeref: 0x11d2

   __TEXT.__swift5_types: 0x6c
   __TEXT.__objc_classname: 0x46c
   __TEXT.__objc_methname: 0x231d
-  __TEXT.__swift5_capture: 0xca4
+  __TEXT.__swift5_capture: 0xc60
   __TEXT.__objc_methtype: 0x1093
   __TEXT.__swift5_protos: 0x50
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0xb50
+  __TEXT.__unwind_info: 0xb70
   __TEXT.__eh_frame: 0x910
-  __DATA_CONST.__auth_got: 0x1048
-  __DATA_CONST.__got: 0x6c8
+  __DATA_CONST.__auth_got: 0x1058
+  __DATA_CONST.__got: 0x6e0
   __DATA_CONST.__auth_ptr: 0x560
-  __DATA_CONST.__const: 0x2908
+  __DATA_CONST.__const: 0x2840
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_const: 0x28f8
   __DATA.__objc_selrefs: 0x890
   __DATA.__objc_data: 0x738
-  __DATA.__data: 0x1270
+  __DATA.__data: 0x1280
   __DATA.__common: 0xb0
   __DATA.__bss: 0x1620
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7BEECB88-10E6-3097-B474-F9CAC1B7EE12
-  Functions: 1186
-  Symbols:   870
-  CStrings:  740
+  UUID: C9B29593-1CD9-3BAF-BFA1-EDFE47A4A27F
+  Functions: 1179
+  Symbols:   874
+  CStrings:  746
 
Symbols:
+ _$s13OSEligibility0A6AnswerO11notEligibleyA2CmFWC
+ _$s13OSEligibility0A6AnswerOSQAAMc
+ _$s13OSEligibility0A6ResultV6result3forAcA0A6DomainO_tKFZ
+ _$sSo13os_log_type_ta0A0E4infoABvgZ
CStrings:
+ "Attempting to reset authorization since current data access level and eligibility do not match"
+ "Failed to get eligibility result, treating as not eligible: %{public}@"
+ "Failed to reset third party data access authorization: %{public}@"
+ "Failed to revoke authorization before attempting to authenticate for non-data access"
+ "Requested authorization for record identifier: %{public}s already approved with data access, but is not eligible for data access, resetting and attempting authorization for non-data access"
+ "com.apple.os-eligibility-domain.change.radium"

```
