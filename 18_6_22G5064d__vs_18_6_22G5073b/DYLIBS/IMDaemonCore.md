## IMDaemonCore

> `/System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore`

```diff

-1402.700.41.0.0
-  __TEXT.__text: 0x2928b8
-  __TEXT.__auth_stubs: 0x44c0
-  __TEXT.__objc_methlist: 0x16a7c
+1402.700.51.0.0
+  __TEXT.__text: 0x2938bc
+  __TEXT.__auth_stubs: 0x44f0
+  __TEXT.__objc_methlist: 0x16ab4
   __TEXT.__const: 0x3608
-  __TEXT.__cstring: 0x12851
-  __TEXT.__gcc_except_tab: 0x27248
+  __TEXT.__cstring: 0x12971
+  __TEXT.__gcc_except_tab: 0x27210
   __TEXT.__oslogstring: 0x45717
-  __TEXT.__ustring: 0x37a
+  __TEXT.__ustring: 0x4d4
   __TEXT.__dlopen_cstrs: 0x128
   __TEXT.__constg_swiftt: 0x10f4
-  __TEXT.__swift5_typeref: 0x17f2
+  __TEXT.__swift5_typeref: 0x1832
   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_reflstr: 0xae8
   __TEXT.__swift5_fieldmd: 0xb4c

   __TEXT.__swift_as_ret: 0xf4
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xadc0
+  __TEXT.__unwind_info: 0xadd8
   __TEXT.__eh_frame: 0x240c
   __TEXT.__objc_classname: 0x2e0a
-  __TEXT.__objc_methname: 0x45a44
+  __TEXT.__objc_methname: 0x45ac3
   __TEXT.__objc_methtype: 0x9386
   __TEXT.__objc_stubs: 0x2c860
-  __DATA_CONST.__got: 0x2b50
+  __DATA_CONST.__got: 0x2b58
   __DATA_CONST.__const: 0x5d68
   __DATA_CONST.__objc_classlist: 0x7b8
-  __DATA_CONST.__objc_catlist: 0xc8
+  __DATA_CONST.__objc_catlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x618
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe528
+  __DATA_CONST.__objc_selrefs: 0xe540
   __DATA_CONST.__objc_protorefs: 0x1e0
   __DATA_CONST.__objc_superrefs: 0x4e0
   __DATA_CONST.__objc_arraydata: 0xb8
-  __AUTH_CONST.__auth_got: 0x2270
+  __AUTH_CONST.__auth_got: 0x2288
   __AUTH_CONST.__const: 0x5870
-  __AUTH_CONST.__cfstring: 0xdfe0
-  __AUTH_CONST.__objc_const: 0x1a708
+  __AUTH_CONST.__cfstring: 0xe0a0
+  __AUTH_CONST.__objc_const: 0x1a748
   __AUTH_CONST.__objc_intobj: 0x918
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x2508
   __AUTH.__data: 0x5c0
   __DATA.__objc_ivar: 0xe98
-  __DATA.__data: 0x4548
+  __DATA.__data: 0x4568
   __DATA.__bss: 0x38f0
   __DATA.__common: 0xe0
   __DATA_DIRTY.__objc_data: 0x3000
-  __DATA_DIRTY.__data: 0x1108
+  __DATA_DIRTY.__data: 0x10f8
   __DATA_DIRTY.__bss: 0xad0
   __DATA_DIRTY.__common: 0x128
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 69E5327D-2667-3425-886F-6E02C9F21B19
-  Functions: 10070
-  Symbols:   2712
-  CStrings:  19538
+  UUID: D1C916C2-5E4A-3197-A9F6-CDA6A88EA3C5
+  Functions: 10084
+  Symbols:   2713
+  CStrings:  19552
 
Symbols:
+ _IMMessageSummaryInfoAssociatedMessagePartText
Functions (added):
+ sub_1d999699c
+ sub_1d99b79e8
+ sub_1d99b8a68
+ sub_1d99d4a84
+ sub_1d99d4b40
+ sub_1d99fb6cc
+ sub_1d9a25ed0
+ [3 functions added in block]
+ sub_1d9a6b2b4
+ sub_1d9a7f238
+ sub_1d9ab3758
+ sub_1d9b504ac
+ sub_1d9b5cc58
+ sub_1d9b87128
+ sub_1d9b8712c
+ sub_1d9b9655c
+ sub_1d9ba0368
+ sub_1d9bae2dc
+ sub_1d9bc8068
+ sub_1d9bc9bb4
+ [3 functions added in block]
+ sub_1d9bca5ac
+ [3 functions added in block]
+ sub_1d9bcad44
+ sub_1d9bcada8
+ sub_1d9bcaea4
+ sub_1d9bcaee8
+ [3 functions added in block]
+ sub_1d9beb280
+ sub_1d9bef020
+ sub_1d9bf02ec

Functions (removed):
- sub_1da4ee350
- sub_1da658b30
- sub_1da667078
- sub_1da66a194
- sub_1da66a600
- sub_1da66af34
- sub_1da66b540
- sub_1da66dcb0
- sub_1da66de4c
- sub_1da66ed80
- sub_1da66edc0
- sub_1da66ee90
- sub_1da66eedc
- sub_1da66f270
- sub_1da66f430
- sub_1da66f848
- sub_1da66f898
- sub_1da66f8e4
- sub_1da67702c
- sub_1da678584
- sub_1da678a50
- sub_1da678abc
- sub_1da678b3c
- sub_1da678b80
- sub_1da678e84
CStrings:
+ "-[IMDFileTransferCenter _messageForFileTransferWithGUID:]"
+ "Attempting to localize string for key: %s, localeID: %s, preferredLocalization: %s, message: %s"
+ "Cancel Button Title"
+ "DaemonCoreLocalization"
+ "Enable Text Message Forwarding: Allow button"
+ "Enable Text Message Forwarding: Cancel button"
+ "RELAY_ENROLLMENT_ALLOW"
+ "RELAY_ENROLLMENT_CANCEL"
+ "RELAY_ENROLLMENT_TEXT_MESSAGE_FORWARDING"
+ "Text Message Forwarding Pin Display Alert arg1: Phone Number, arg2: a 6 digit code"
+ "Title: Text Message Forwarding"
+ "Unable to load IMDaemonCoreBundle"
+ "__im_localizedStringForKey:"
+ "__im_localizedStringForKey:comment:"
+ "_hasSavedContactCardForHandle:"
+ "_isFileTransferWithGUIDFromKnownSender:"
+ "_messageForFileTransferWithGUID:"
- "-[IMDFileTransferCenter _findTransferGUIDMatchingSpotlightDonatedSpeculativeTransferGUID:]"
- "Allow"
- "Attempting to localize string for localeID: %@, preferredLocalization: %@, message: %@"
- "Cancel"
- "Current aliasToCNIDMap %@"
- "Found contactID: %@ for handle: %@"
- "Text Message Forwarding"
- "_localizedStringForKey:"
- "localeIdentifier"

```
