## SiriContactsIntents

> `/System/Library/PrivateFrameworks/SiriContactsIntents.framework/SiriContactsIntents`

```diff

-3400.74.1.0.0
-  __TEXT.__text: 0xee1bc
-  __TEXT.__auth_stubs: 0x4230
+3400.80.1.0.0
+  __TEXT.__text: 0xef918
+  __TEXT.__auth_stubs: 0x4250
   __TEXT.__objc_methlist: 0x87c
   __TEXT.__const: 0x6460
   __TEXT.__cstring: 0x6585
-  __TEXT.__swift5_typeref: 0x1bd2
-  __TEXT.__swift5_capture: 0x288
-  __TEXT.__oslogstring: 0x795b
+  __TEXT.__swift5_typeref: 0x1bd0
+  __TEXT.__swift5_capture: 0x28c
+  __TEXT.__oslogstring: 0x7ceb
   __TEXT.__swift5_fieldmd: 0x1e48
-  __TEXT.__constg_swiftt: 0x3470
+  __TEXT.__constg_swiftt: 0x3478
   __TEXT.__swift5_builtin: 0x118
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_reflstr: 0x1bd6

   __TEXT.__swift5_types: 0x230
   __TEXT.__swift5_assocty: 0x650
   __TEXT.__swift5_proto: 0x38c
-  __TEXT.__unwind_info: 0x3818
-  __TEXT.__eh_frame: 0x87d0
+  __TEXT.__unwind_info: 0x38d8
+  __TEXT.__eh_frame: 0x8a70
   __TEXT.__objc_classname: 0xaa
-  __TEXT.__objc_methname: 0x1b68
+  __TEXT.__objc_methname: 0x1ba9
   __TEXT.__objc_methtype: 0x1a8
-  __DATA_CONST.__got: 0x11c8
-  __DATA_CONST.__const: 0x598
+  __DATA_CONST.__got: 0x11d0
+  __DATA_CONST.__const: 0x5d8
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x890
+  __DATA_CONST.__objc_selrefs: 0x8b0
   __DATA_CONST.__objc_protorefs: 0x80
-  __AUTH_CONST.__auth_got: 0x2118
-  __AUTH_CONST.__auth_ptr: 0xfe0
+  __AUTH_CONST.__auth_got: 0x2128
+  __AUTH_CONST.__auth_ptr: 0xf00
   __AUTH_CONST.__const: 0x46a8
   __AUTH_CONST.__objc_const: 0x62a8
   __AUTH.__objc_data: 0x1bd0
   __AUTH.__data: 0x2a50
-  __DATA.__data: 0x20a8
+  __DATA.__data: 0x2098
   __DATA.__objc_stublist: 0x18
   __DATA.__bss: 0x5e80
   __DATA.__common: 0x218

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5286
-  Symbols:   9394
-  CStrings:  1513
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 5303
+  Symbols:   9424
+  CStrings:  1526
 
Symbols:
+ _$s11SiriKitFlow11DeviceStateP15isAuthenticated3forSbAA06UnlockD6PolicyV_tFTj
+ _$s18SiriContactsCommon14CodableContactV12wrappedValuexvg
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "#ContactsUnsetRelationshipFlowStrategy actionForPromptForContactDisambiguationInput"
+ "#ContactsUnsetRelationshipFlowStrategy actionForPromptForNameInput"
+ "#ContactsUnsetRelationshipFlowStrategy actionForPromptToSaveRelationship"
+ "#ContactsUnsetRelationshipFlowStrategy unsetRelationshipActionForInput"
+ "#ContactsUnsetRelationshipFlowStrategy unsetRelationshipActionForInput detected a confirmation or disambig response, deferring to getActionForInput"
+ "#ContactsUnsetRelationshipFlowStrategy: Received a non-update-person task type, returning .ignore()"
+ "#ContactsUnsetRelationshipFlowStrategy: confirmation response parse, returning .handle()"
+ "#ContactsUnsetRelationshipFlowStrategy: disambiguation task parse, returning .handle()"
+ "ModifyContactAttributeSnippetModel couldn't fetch related contact for display, falling back on empty one"
+ "contactWithDisplayName:handleStrings:"
+ "emptyContact"
+ "prefix"
+ "suffix"

```
