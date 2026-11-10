## FamilyOutOfProcessUIExtension

> `/System/Library/CoreServices/FamilyExtensionHost.app/Contents/Extensions/FamilyOutOfProcessUIExtension.appex/Contents/MacOS/FamilyOutOfProcessUIExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_entry`

```diff

-290.3.1.0.0
-  __TEXT.__text: 0xd29c
-  __TEXT.__auth_stubs: 0xc70
-  __TEXT.__objc_stubs: 0x320
-  __TEXT.__const: 0x852
-  __TEXT.__constg_swiftt: 0x19c
-  __TEXT.__swift5_typeref: 0x939
-  __TEXT.__swift5_reflstr: 0x1e6
-  __TEXT.__swift5_fieldmd: 0x158
+291.125.8.0.0
+  __TEXT.__text: 0x15dc8
+  __TEXT.__auth_stubs: 0x11e0
+  __TEXT.__objc_stubs: 0x3a0
+  __TEXT.__const: 0xa22
+  __TEXT.__constg_swiftt: 0x260
+  __TEXT.__swift5_typeref: 0xb0b
+  __TEXT.__swift5_reflstr: 0x226
+  __TEXT.__swift5_fieldmd: 0x1bc
+  __TEXT.__swift5_assocty: 0xf0
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_assocty: 0xd8
-  __TEXT.__swift5_proto: 0x4c
-  __TEXT.__swift5_types: 0x18
+  __TEXT.__swift5_proto: 0x54
+  __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__objc_classname: 0x43
-  __TEXT.__objc_methname: 0x265
-  __TEXT.__objc_methtype: 0x8f
-  __TEXT.__swift5_capture: 0x108
-  __TEXT.__oslogstring: 0x302
-  __TEXT.__cstring: 0x1c5
-  __TEXT.__swift_as_entry: 0x20
-  __TEXT.__swift_as_ret: 0x34
-  __TEXT.__swift_as_cont: 0x74
-  __TEXT.__unwind_info: 0x4a8
-  __TEXT.__eh_frame: 0x8a0
-  __DATA_CONST.__const: 0x478
-  __DATA_CONST.__objc_classlist: 0x8
+  __TEXT.__swift5_capture: 0x178
+  __TEXT.__cstring: 0x41e
+  __TEXT.__objc_methtype: 0xcf
+  __TEXT.__oslogstring: 0x462
+  __TEXT.__swift_as_entry: 0x50
+  __TEXT.__swift_as_ret: 0x6c
+  __TEXT.__swift_as_cont: 0x10c
+  __TEXT.__objc_methname: 0x2eb
+  __TEXT.__unwind_info: 0x730
+  __TEXT.__eh_frame: 0x1388
+  __DATA_CONST.__const: 0x638
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x640
-  __DATA_CONST.__got: 0x200
-  __DATA_CONST.__auth_ptr: 0x398
-  __DATA.__objc_const: 0xb8
-  __DATA.__objc_selrefs: 0xc8
-  __DATA.__data: 0x520
-  __DATA.__bss: 0x990
+  __DATA_CONST.__auth_got: 0x8f8
+  __DATA_CONST.__got: 0x318
+  __DATA_CONST.__auth_ptr: 0x3f0
+  __DATA.__objc_selrefs: 0xe8
+  __DATA.__data: 0x648
+  __DATA.__bss: 0xab8
+  - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/ExtensionFoundation.framework/Versions/A/ExtensionFoundation
   - /System/Library/Frameworks/ExtensionKit.framework/Versions/A/ExtensionKit
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/Versions/A/SwiftUI
-  - /System/Library/PrivateFrameworks/AAAFoundationSwift.framework/Versions/A/AAAFoundationSwift
+  - /System/Library/PrivateFrameworks/AAAFoundationUI.framework/Versions/A/AAAFoundationUI
   - /System/Library/PrivateFrameworks/FamilyCircle.framework/Versions/A/FamilyCircle
   - /System/Library/PrivateFrameworks/FamilyCircleUI.framework/Versions/A/FamilyCircleUI
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/Versions/A/OnBoardingKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 257
-  Symbols:   105
-  CStrings:  53
+  Functions: 372
+  Symbols:   122
+  CStrings:  84
 
Symbols:
+ _OBJC_CLASS_$_ACAccountStore
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSXPCConnection
+ ___assert_rtn
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __availability_version_check
+ _dispatch_once_f
+ _dlsym
+ _fclose
+ _fopen
+ _fread
+ _free
+ _fseek
+ _ftell
+ _malloc
+ _rewind
+ _sscanf
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain_n
+ _swift_dynamicCast
+ _swift_task_future_wait_throwing
- _OBJC_CLASS_$__TtCs12_SwiftObject
- _OBJC_METACLASS_$__TtCs12_SwiftObject
- __objc_empty_cache
- _swift_deallocClassInstance
- _swift_deletedMethodError
CStrings:
+ "%d.%d.%d"
+ "/System/Library/CoreServices/SystemVersion.plist"
+ "CFDataCreateWithBytesNoCopy"
+ "CFDictionaryGetValue"
+ "CFGetTypeID"
+ "CFPropertyListCreateFromXMLData"
+ "CFPropertyListCreateWithData"
+ "CFRelease"
+ "CFStringCreateWithCStringNoCopy"
+ "CFStringGetCString"
+ "CFStringGetTypeID"
+ "EntryView task ran with nil requestModel, waiting for scene context"
+ "Failed to terminate extension: %s"
+ "Non-UI: applyScreentimeSettings rejected, missing %s"
+ "Non-UI: getUserAge rejected, missing %s"
+ "Non-UI: rejecting connection, missing %s"
+ "Non-UI: shouldPromptAgeRange rejected, missing %s"
+ "Platform2 == PLATFORM_MACOS && \"unexpected platform\""
+ "ProductVersion"
+ "View.task @ FamilyOutOfProcessUIExtension/FamilyOutOfProcessUIExtension.swift:"
+ "__isPlatformOrVariantPlatformVersionAtLeast"
+ "aa_altDSID"
+ "aa_primaryAppleAccountWithCompletion:"
+ "boolValue"
+ "cachedAgeRangeResponseWith:userAgeOverride:bundleID:attestedAtOverrideInDays:completion:"
+ "code"
+ "com.apple.developer.declared-age-range"
+ "com.apple.family.ageRange"
+ "com.apple.private.ageRange"
+ "com.apple.private.familycircle"
+ "defaultStore"
+ "initWithInteger:"
+ "kCFAllocatorNull"
+ "os_version_check.c"
+ "r"
+ "removingNonSecureCodingValues"
+ "v24@?0@\"ACAccount\"8@\"NSError\"16"
+ "v24@?0@\"FAAgeRangeResponse\"8@\"NSError\"16"
+ "valueForEntitlement:"
- "AgeRangeAlertFlowStore"
- "_TtC29FamilyOutOfProcessUIExtension29FamilyOutOfProcessUIExtension"
- "ageGates"
- "ageRangeController"
- "attestedAtOverrideInDays"
- "entryPoint"
- "requestType"
- "userAgeOverride"
```
