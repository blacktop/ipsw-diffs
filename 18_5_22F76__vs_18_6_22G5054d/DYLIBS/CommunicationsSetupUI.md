## CommunicationsSetupUI

> `/System/Library/PrivateFrameworks/CommunicationsSetupUI.framework/CommunicationsSetupUI`

```diff

-1500.600.1.2.1
-  __TEXT.__text: 0x82754
+1500.700.1.0.0
+  __TEXT.__text: 0x82418
   __TEXT.__auth_stubs: 0x1170
   __TEXT.__objc_methlist: 0x81cc
-  __TEXT.__cstring: 0xa887
+  __TEXT.__cstring: 0xa877
   __TEXT.__const: 0x4c4
-  __TEXT.__gcc_except_tab: 0x4828
-  __TEXT.__oslogstring: 0x5a6d
+  __TEXT.__gcc_except_tab: 0x47f8
+  __TEXT.__oslogstring: 0x5a11
   __TEXT.__dlopen_cstrs: 0x62
   __TEXT.__ustring: 0x40
   __TEXT.__swift5_typeref: 0x250

   __TEXT.__swift5_types: 0x18
   __TEXT.__unwind_info: 0x2668
   __TEXT.__objc_classname: 0x1038
-  __TEXT.__objc_methname: 0x14232
+  __TEXT.__objc_methname: 0x1423d
   __TEXT.__objc_methtype: 0x3846
-  __TEXT.__objc_stubs: 0xfce0
+  __TEXT.__objc_stubs: 0xfd00
   __DATA_CONST.__got: 0xa98
   __DATA_CONST.__const: 0x1100
   __DATA_CONST.__objc_classlist: 0x318
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x54c0
+  __DATA_CONST.__objc_selrefs: 0x54c8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x270
   __DATA_CONST.__objc_arraydata: 0x98

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 29303694-1E67-3D35-ABA9-9BC98BD5E96A
+  UUID: B6BC6410-FB18-3D02-A9E0-A81DA3CD54AF
   Functions: 2803
-  Symbols:   9988
+  Symbols:   9989
   CStrings:  7034
 
Symbols:
+ _objc_msgSend$regionCode
Functions:
~ -[CNFRegSettingsController _safetyURLForCurrentRegionIfAny] : 936 -> 768
~ -[CKSettingsMessagesController currentRegionWantsOnlineSafetyLink] : 784 -> 304
~ -[CKSettingsMessagesController _safetyURLForCurrentRegion] : 360 -> 180
CStrings:
+ "GB"
+ "ONLINE SAFETY: Checking if region %@ requires safety URL to be shown..."
+ "ONLINE SAFETY: No valid safety URL was found for any of user's region"
+ "Region: %@ wanted to show the online safety link"
+ "regionCode"
- "Domain: %@ wanted to show the online safety link"
- "ONLINE SAFETY: Checking if region estimate %@ requires safety URL to be shown..."
- "ONLINE SAFETY: No valid safety URL was found for any of user's region estimates"
- "UK"
- "Unable to determine region, defaulting to not showing online safety link"

```
