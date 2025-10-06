## UARPUpdaterServiceHID

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceHID.xpc/UARPUpdaterServiceHID`

```diff

-916.0.46.0.0
-  __TEXT.__text: 0x17904
-  __TEXT.__auth_stubs: 0x710
-  __TEXT.__objc_stubs: 0x23e0
-  __TEXT.__objc_methlist: 0x9c4
+916.40.22.0.2
+  __TEXT.__text: 0x186e8
+  __TEXT.__auth_stubs: 0x740
+  __TEXT.__objc_stubs: 0x24c0
+  __TEXT.__objc_methlist: 0x9f4
   __TEXT.__gcc_except_tab: 0xa4
-  __TEXT.__objc_methname: 0x3208
+  __TEXT.__objc_methname: 0x330d
   __TEXT.__objc_classname: 0x1ac
-  __TEXT.__objc_methtype: 0xac5
-  __TEXT.__cstring: 0x1647
-  __TEXT.__oslogstring: 0xe0b
+  __TEXT.__objc_methtype: 0xab3
+  __TEXT.__cstring: 0x1611
+  __TEXT.__oslogstring: 0xec1
   __TEXT.__const: 0x38
-  __TEXT.__unwind_info: 0x608
-  __DATA_CONST.__auth_got: 0x398
+  __TEXT.__unwind_info: 0x614
+  __DATA_CONST.__auth_got: 0x3b0
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__const: 0x670
-  __DATA_CONST.__cfstring: 0x400
+  __DATA_CONST.__cfstring: 0x420
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x25c0
-  __DATA.__objc_selrefs: 0xab0
+  __DATA.__objc_const: 0x25e0
+  __DATA.__objc_selrefs: 0xaf8
   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x130
   __DATA.__objc_superrefs: 0x38
-  __DATA.__objc_ivar: 0xc8
+  __DATA.__objc_ivar: 0xcc
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x30a
   __DATA.__bss: 0x368

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 62B1A4D5-9CDC-30CE-8D59-F61BFBAB4B75
-  Functions: 627
-  Symbols:   442
-  CStrings:  898
+  UUID: 51002879-26B2-383D-9ADA-255BAEED99B9
+  Functions: 639
+  Symbols:   445
+  CStrings:  911
 
Symbols:
+ _UARPAccessoryTransportToString
+ _createPowerAssertion
+ _releasePowerAssertion
CStrings:
+ "\x04"
+ "\x04\x12\x13!"
+ "%s: Accessory Identifier %@ auro-applies firmware "
+ "Already holding power assertion for %@ refCount=%u"
+ "Already released power assertion for %@"
+ "Failed to create power assertion for %@"
+ "Failed to release power assertion for %@"
+ "Power assertion ref count invalid for %@"
+ "_powerAssertionID"
+ "_powerAssertionRefCount"
+ "autoAppliesStagedFirmware"
+ "com.apple.UARPPowerAssertion-%s"
+ "getAccessoriesForIdentifier:"
+ "holdPowerAssertionForAccessory:"
+ "matchingDictionaryForIdentifier:"
+ "matchingDictionaryForVendorID:productID:"
+ "modelIdentifier"
+ "personalities"
+ "personalityIdentifier:"
+ "releasePowerAssertionForAccessory:"
+ "updateRequiresPowerAssertion"
- "\x04\x12\x13\x11"
- "\x05"
- "%s: RegistryEntryID found 0x%llx for identifier %@"
- "%s: Supported HID Accessory %@"
- "-[UARPUpdaterServiceHID init]"
- "-[UARPUpdaterServiceHID registryEntryIDsForIdentifier:]"
- "@\"NSMutableArray\""
- "_supportedAccessories"
- "getAccessoriesForIdentifier:hardwareID:"

```
