## EventKitUI

> `/System/Library/Frameworks/EventKitUI.framework/EventKitUI`

```diff

-1529.2.1.0.0
-  __TEXT.__text: 0x1dc454
+1529.2.3.0.0
+  __TEXT.__text: 0x1dcc2c
   __TEXT.__auth_stubs: 0x2250
-  __TEXT.__objc_methlist: 0x1f1b4
-  __TEXT.__const: 0x2874
-  __TEXT.__cstring: 0xdcf1
+  __TEXT.__objc_methlist: 0x1f1e4
+  __TEXT.__const: 0x2894
+  __TEXT.__cstring: 0xdd81
   __TEXT.__gcc_except_tab: 0x434c
-  __TEXT.__oslogstring: 0x78bd
+  __TEXT.__oslogstring: 0x793d
   __TEXT.__ustring: 0x862
   __TEXT.__dlopen_cstrs: 0x322
   __TEXT.__swift5_typeref: 0xd4e

   __TEXT.__swift5_types: 0xf8
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
-  __TEXT.__unwind_info: 0x77b0
+  __TEXT.__unwind_info: 0x77d8
   __TEXT.__eh_frame: 0x5d0
   __TEXT.__objc_classname: 0x427b
-  __TEXT.__objc_methname: 0x4584c
+  __TEXT.__objc_methname: 0x458f8
   __TEXT.__objc_methtype: 0xc36f
-  __TEXT.__objc_stubs: 0x32080
+  __TEXT.__objc_stubs: 0x320c0
   __DATA_CONST.__got: 0x1970
-  __DATA_CONST.__const: 0x46e8
+  __DATA_CONST.__const: 0x4778
   __DATA_CONST.__objc_classlist: 0xc60
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x628
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf6a8
+  __DATA_CONST.__objc_selrefs: 0xf6d0
   __DATA_CONST.__objc_protorefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x8b8
   __DATA_CONST.__objc_arraydata: 0x1c0
   __AUTH_CONST.__auth_got: 0x1138
   __AUTH_CONST.__const: 0x2808
-  __AUTH_CONST.__cfstring: 0xb2a0
-  __AUTH_CONST.__objc_const: 0x30758
+  __AUTH_CONST.__cfstring: 0xb3a0
+  __AUTH_CONST.__objc_const: 0x30788
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_intobj: 0x570
   __AUTH_CONST.__objc_doubleobj: 0x70

   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x7be8
   __AUTH.__data: 0xbc0
-  __DATA.__objc_ivar: 0x2544
+  __DATA.__objc_ivar: 0x2548
   __DATA.__data: 0x4bc0
-  __DATA.__bss: 0x1630
+  __DATA.__bss: 0x1640
   __DATA.__common: 0x218
   __DATA_DIRTY.__objc_data: 0x13b0
   __DATA_DIRTY.__bss: 0x20

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 89D3FA7A-13F0-30F4-8BCE-A04D2AD7172F
-  Functions: 11801
-  Symbols:   35005
-  CStrings:  16466
+  UUID: 0E35BFAD-BA0B-37CD-BD00-96AE3D1A3C4D
+  Functions: 11810
+  Symbols:   35031
+  CStrings:  16492
 
Symbols:
+ +[EKDayOccurrenceView hasPerformedSynchronousRendering]
+ +[EKDayViewContentItem hasRequestedSynchronousRendering]
+ -[EKEventViewController requestedResponse]
+ -[EKEventViewController setRequestedResponse:]
+ GCC_except_table100
+ GCC_except_table110
+ GCC_except_table121
+ GCC_except_table127
+ GCC_except_table135
+ GCC_except_table139
+ GCC_except_table141
+ GCC_except_table143
+ GCC_except_table145
+ GCC_except_table149
+ GCC_except_table151
+ GCC_except_table156
+ GCC_except_table204
+ GCC_except_table33
+ GCC_except_table75
+ _EKUIEventDetailsContext_Response
+ _OBJC_IVAR_$_EKEventViewController._requestedResponse
+ _PresentRespondingToUnknownSenderAlert
+ ___PresentRespondingToUnknownSenderAlert_block_invoke
+ ___PresentRespondingToUnknownSenderAlert_block_invoke.46
+ ___PresentRespondingToUnknownSenderAlert_block_invoke_2
+ ___block_descriptor_40_e23_v16?0"UIAlertAction"8l
+ ___block_descriptor_48_e8_32s_e23_v16?0"UIAlertAction"8ls32l8
+ ___block_descriptor_56_e8_32s_e23_v16?0"UIAlertAction"8ls32l8
+ ___block_literal_global.280
+ ___block_literal_global.294
+ _hasPerformedSynchronousRendering
+ _hasRequestedSynchronousRendering
+ _objc_msgSend$setParticipantStatus:
+ _objc_msgSend$setRequestedResponse:
+ _reportLinkedJunkInvitationAction
- GCC_except_table109
- GCC_except_table120
- GCC_except_table126
- GCC_except_table128
- GCC_except_table134
- GCC_except_table138
- GCC_except_table140
- GCC_except_table142
- GCC_except_table144
- GCC_except_table146
- GCC_except_table150
- GCC_except_table154
- GCC_except_table157
- GCC_except_table203
- GCC_except_table72
- GCC_except_table87
- ___block_literal_global.279
- ___block_literal_global.293
CStrings:
+ "Accept Invitation"
+ "Decline Invitation"
+ "Displaying unknown sender alert for event for response %lu"
+ "EKUIEventDetailsContext_Response"
+ "Error responding to event: %@"
+ "Responding to event with new status %lu"
+ "TQ,N,V_requestedResponse"
+ "Tentatively Accept Invitation"
+ "View Invitation"
+ "_requestedResponse"
+ "hasPerformedSynchronousRendering"
+ "hasRequestedSynchronousRendering"
+ "junkInviteLinkAction"
+ "reply"
+ "requestedResponse"
+ "setParticipantStatus:"
+ "setRequestedResponse:"

```
