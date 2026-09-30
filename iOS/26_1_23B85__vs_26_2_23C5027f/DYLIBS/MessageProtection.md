## MessageProtection

> `/System/Library/PrivateFrameworks/MessageProtection.framework/MessageProtection`

```diff

-385.0.7.0.0
-  __TEXT.__text: 0x836c0
+385.60.2.0.0
+  __TEXT.__text: 0x83418
   __TEXT.__auth_stubs: 0x2180
   __TEXT.__objc_methlist: 0x2374
   __TEXT.__const: 0x5430
-  __TEXT.__cstring: 0x3e01
-  __TEXT.__oslogstring: 0x26b1
+  __TEXT.__cstring: 0x3dc1
+  __TEXT.__oslogstring: 0x2621
   __TEXT.__gcc_except_tab: 0x598
   __TEXT.__ustring: 0x21c
   __TEXT.__constg_swiftt: 0x12f4

   __TEXT.__swift5_reflstr: 0x1117
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_assocty: 0x1c8
-  __TEXT.__unwind_info: 0x1e70
+  __TEXT.__unwind_info: 0x1e50
   __TEXT.__eh_frame: 0x2e00
   __TEXT.__objc_classname: 0x58c
-  __TEXT.__objc_methname: 0x3f5d
+  __TEXT.__objc_methname: 0x3f2e
   __TEXT.__objc_methtype: 0xc49
-  __TEXT.__objc_stubs: 0x2e20
-  __DATA_CONST.__got: 0x5f0
-  __DATA_CONST.__const: 0x3d0
+  __TEXT.__objc_stubs: 0x2dc0
+  __DATA_CONST.__got: 0x5e8
+  __DATA_CONST.__const: 0x3c8
   __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf88
+  __DATA_CONST.__objc_selrefs: 0xf70
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x128
   __AUTH_CONST.__auth_got: 0x10d0
   __AUTH_CONST.__const: 0x25c8
-  __AUTH_CONST.__cfstring: 0x1900
+  __AUTH_CONST.__cfstring: 0x18a0
   __AUTH_CONST.__objc_const: 0x6200
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH.__objc_data: 0x330

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 39B574A1-1DBA-3543-9599-F12109E755C3
-  Functions: 2574
-  Symbols:   10186
-  CStrings:  1664
+  UUID: E68FD4D3-C63B-3AB4-9B43-20651B96396B
+  Functions: 2568
+  Symbols:   10168
+  CStrings:  1654
 
Symbols:
- _MPSecondaryEncryptionDisabled
- _MPSecondaryRegistrationDisabled
- _MPSetSecondaryEncryptionDisabled
- _MPSetSecondaryRegistrationDisabled
- _OBJC_CLASS_$_NSUserDefaults
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit_$_MessageProtection
- _get_value
- _objc_msgSend$boolForKey:
- _objc_msgSend$initWithSuiteName:
- _objc_msgSend$setBool:forKey:
- _set_value
CStrings:
+ "Identity is not identical since the Tetra version has been lowered."
+ "Re-registering because of Tetra update."
+ "Sealing message with GUID: %@."
- "Re-registering because of Tetra update or an enablement."
- "Re-registering with a fresh prekey because Tetra was disabled and we still have a prekey with secondary registration."
- "Sealing message with GUID: %@. secondaryDisabled=%d, secondaryRegistrationDisabled=%d"
- "SecondaryEncryptionDisabled"
- "SecondaryRegistrationDisabled"
- "Tetra version has been lowered."
- "boolForKey:"
- "com.apple.ids"
- "initWithSuiteName:"
- "setBool:forKey:"

```
