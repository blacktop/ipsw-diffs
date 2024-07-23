## feedbackd

> `/usr/libexec/feedbackd`

```diff

-120.0.0.0.0
-  __TEXT.__text: 0x6162c
-  __TEXT.__auth_stubs: 0x1b40
+124.0.0.0.0
+  __TEXT.__text: 0x63bf0
+  __TEXT.__auth_stubs: 0x1c30
   __TEXT.__objc_methlist: 0x20c
   __TEXT.__const: 0x14f0
-  __TEXT.__cstring: 0x2761
-  __TEXT.__objc_methname: 0x143e
-  __TEXT.__swift5_typeref: 0xba1
-  __TEXT.__swift5_capture: 0x464
-  __TEXT.__constg_swiftt: 0xa7c
-  __TEXT.__swift5_reflstr: 0xa3e
-  __TEXT.__swift5_fieldmd: 0x7bc
-  __TEXT.__oslogstring: 0x1db8
+  __TEXT.__cstring: 0x28f6
+  __TEXT.__objc_methname: 0x144e
+  __TEXT.__swift5_typeref: 0xbc9
+  __TEXT.__swift5_capture: 0x4b0
+  __TEXT.__constg_swiftt: 0xa84
+  __TEXT.__swift5_reflstr: 0xa4e
+  __TEXT.__swift5_fieldmd: 0x7c8
+  __TEXT.__oslogstring: 0x1f08
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_assocty: 0x120
   __TEXT.__swift5_proto: 0xec

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_entry: 0x8
   __TEXT.__info_plist: 0x3fe
-  __TEXT.__unwind_info: 0x1268
-  __TEXT.__eh_frame: 0x30f8
-  __DATA_CONST.__auth_got: 0xda0
-  __DATA_CONST.__got: 0x680
-  __DATA_CONST.__auth_ptr: 0x3d0
-  __DATA_CONST.__const: 0x1640
+  __TEXT.__unwind_info: 0x12c8
+  __TEXT.__eh_frame: 0x3238
+  __DATA_CONST.__auth_got: 0xe18
+  __DATA_CONST.__got: 0x6b0
+  __DATA_CONST.__auth_ptr: 0x3d8
+  __DATA_CONST.__const: 0x16b8
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA.__objc_const: 0x1f48
-  __DATA.__objc_selrefs: 0x588
+  __DATA.__objc_selrefs: 0x590
   __DATA.__objc_data: 0x8e8
-  __DATA.__data: 0x1968
-  __DATA.__bss: 0x1d90
+  __DATA.__data: 0x19a8
+  __DATA.__bss: 0x1db8
   __DATA.__common: 0xb8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1245
-  Symbols:   744
-  CStrings:  676
+  Functions: 1270
+  Symbols:   762
+  CStrings:  699
 
Symbols:
+ _$s15FeedbackService12FBKSDonationC13DonationErrorO11unsupportedyA2EmFWC
+ _$s15FeedbackService15FBKSInteractionC13FeatureDomainO11swiftAssistyA2EmFWC
+ _$s15FeedbackService15FBKSInteractionC13FeatureDomainOSHAAMc
+ _$s15FeedbackService15FBKSInteractionC13FeatureDomainOSQAAMc
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _CFNotificationCenterPostNotification
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
+ _swift_stdlib_random
- _$s15FeedbackService12FBKSDonationC13DonationErrorO8disabledyA2EmFWC
CStrings:
+ "%!d(MISSING).%!d(MISSING).%!d(MISSING)"
+ "%!{(MISSING)public}s error: Failed to access the FeedbackInternal UserDefaults from daemonHi ."
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
+ "Changing the visibility of FeedbackInternal app."
+ "Configuring internal app visibility."
+ "Donation dropped due to sampling: %!{(MISSING)private,mask.hash}s"
+ "Donation error: %!s(MISSING)"
+ "Donation not enabled"
+ "FeedbackInternal is already visible."
+ "ProductVersion"
+ "SBIconVisibility"
+ "_donate(donationJSON:completion:)"
+ "_recordEvaluation(evaluation:isInline:)"
+ "com.apple.springboard.appIconVisibilityPreferencesChanged"
+ "kCFAllocatorNull"
+ "r"
+ "setBool:forKey:"
- "Donation currently disabled on Seed Builds"
- "_recordEvaluation(evaluation:)"
- "donate(donationJSON:completion:)"

```
