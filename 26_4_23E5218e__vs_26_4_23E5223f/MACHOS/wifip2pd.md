## wifip2pd

> `/usr/libexec/wifip2pd`

```diff

-855.30.4.1.0
-  __TEXT.__text: 0x4de3fc
-  __TEXT.__auth_stubs: 0x4950
+855.32.0.0.0
+  __TEXT.__text: 0x4e00f0
+  __TEXT.__auth_stubs: 0x49b0
   __TEXT.__objc_stubs: 0x3b20
   __TEXT.__objc_methlist: 0x177c
-  __TEXT.__const: 0x390f8
-  __TEXT.__swift5_typeref: 0xb43e
+  __TEXT.__const: 0x39008
+  __TEXT.__swift5_typeref: 0xb3fe
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0xa77e
-  __TEXT.__oslogstring: 0x16adc
-  __TEXT.__constg_swiftt: 0xe07c
-  __TEXT.__swift5_fieldmd: 0x1464c
+  __TEXT.__cstring: 0xa7ca
+  __TEXT.__oslogstring: 0x16e5c
+  __TEXT.__constg_swiftt: 0xe080
+  __TEXT.__swift5_fieldmd: 0x14640
   __TEXT.__swift5_types: 0x10b0
-  __TEXT.__swift5_reflstr: 0x126d6
-  __TEXT.__swift5_builtin: 0x157c
+  __TEXT.__swift5_reflstr: 0x126f6
+  __TEXT.__swift5_builtin: 0x1590
   __TEXT.__swift5_assocty: 0x2958
   __TEXT.__swift5_protos: 0xe8
-  __TEXT.__swift5_proto: 0x2b44
+  __TEXT.__swift5_proto: 0x2b30
   __TEXT.__objc_classname: 0xd39
   __TEXT.__objc_methtype: 0x1bc7
-  __TEXT.__objc_methname: 0x8775
-  __TEXT.__swift5_capture: 0x4c14
+  __TEXT.__objc_methname: 0x8795
+  __TEXT.__swift5_capture: 0x4c3c
   __TEXT.__swift5_mpenum: 0x16c
   __TEXT.__swift_as_entry: 0x110
   __TEXT.__swift_as_ret: 0xb0
-  __TEXT.__unwind_info: 0xdc90
+  __TEXT.__unwind_info: 0xdc88
   __TEXT.__eh_frame: 0x18130
-  __DATA_CONST.__auth_got: 0x24b0
-  __DATA_CONST.__got: 0xed8
+  __DATA_CONST.__auth_got: 0x24e0
+  __DATA_CONST.__got: 0xf00
   __DATA_CONST.__auth_ptr: 0x1e30
-  __DATA_CONST.__const: 0x2ef30
+  __DATA_CONST.__const: 0x2ef78
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x138
-  __DATA.__objc_const: 0x8b48
+  __DATA.__objc_const: 0x8b68
   __DATA.__objc_selrefs: 0x12f0
   __DATA.__objc_data: 0x1390
-  __DATA.__data: 0x11370
+  __DATA.__data: 0x11380
   __DATA.__common: 0x8e8
-  __DATA.__bss: 0x543c0
+  __DATA.__bss: 0x54140
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/IO80211.framework/IO80211
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/Netrb.framework/Netrb
+  - /System/Library/PrivateFrameworks/OSEligibility.framework/OSEligibility
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 356DCCA6-C483-39A8-966F-AF5367F7FE24
-  Functions: 21152
-  Symbols:   2129
-  CStrings:  4247
+  UUID: 75305DCC-6460-36D4-A0A8-E5037B46EEFB
+  Functions: 21153
+  Symbols:   2140
+  CStrings:  4263
 
Symbols:
+ _$s13OSEligibility0A6AnswerO11notEligibleyA2CmFWC
+ _$s13OSEligibility0A6AnswerO15notYetAvailableyA2CmFWC
+ _$s13OSEligibility0A6AnswerO2eeoiySbAC_ACtFZ
+ _$s13OSEligibility0A6AnswerO5maybeyA2CmFWC
+ _$s13OSEligibility0A6AnswerO8eligibleyA2CmFWC
+ _$s13OSEligibility0A6AnswerOMa
+ _$s13OSEligibility0A6DomainO8poloniumyA2CmFWC
+ _$s13OSEligibility0A6DomainOMa
+ _$s13OSEligibility0A6ResultV6answerAA0A6AnswerOvg
+ _$s13OSEligibility0A6ResultV6result3forAcA0A6DomainO_tKFZ
+ _$s13OSEligibility0A6ResultVMa
CStrings:
+ "5G/160 Notification already registered"
+ "Failed to parse the action frame contents from %s as a vendor specific NAN action frame. Received frame category=%hhu, contents type: %s"
+ "Failed to register for 5G/160 OS eligibility notifications: status=%u"
+ "Failed to update OS eligibility for 5G 160: %@"
+ "NANActionFrame: Found and stripped MMIE at offset %ld, total MMIE size=%ld, new payload length=%ld"
+ "NANActionFrame: Successfully decoded %ld attributes"
+ "NANActionFrame: decoding attributes, remaining data length=%ld, hex=%s"
+ "OS Eligibility for 5G/160 change notification received"
+ "OS Eligibility: 5G/160 = DISABLED not eligible(%{bool}d)"
+ "OS Eligibility: 5G/160 = ENABLED"
+ "OS Eligibility: 5G/160 answer %s"
+ "Registered for 5G/160 OS eligibility change notifications (token=%d)"
+ "Successfully sent OS eligibility for 5G 160"
+ "Unregistered 5G/160 OS eligibility notifications (token=%d)"
+ "WiFiP2P-855.32 Feb 26 2026 23:02:52"
+ "com.apple.os-eligibility-domain.change.polonium"
+ "not yet available"
+ "notificationToken5G160"
- "Failed to parse the action frame contents from %s as a vendor specific NAN action frame"
- "WiFiP2P-855.30.4.1 Feb 17 2026 21:02:39"

```
