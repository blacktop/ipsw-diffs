## trustd

> `/usr/libexec/trustd`

```diff

-61901.40.47.0.1
-  __TEXT.__text: 0x5f498
+61901.40.71.0.2
+  __TEXT.__text: 0x6020c
   __TEXT.__auth_stubs: 0x23c0
-  __TEXT.__objc_stubs: 0x2d00
-  __TEXT.__objc_methlist: 0xc0c
-  __TEXT.__const: 0x59a1
-  __TEXT.__gcc_except_tab: 0xd48
-  __TEXT.__cstring: 0x674b
-  __TEXT.__oslogstring: 0x5a8e
+  __TEXT.__objc_stubs: 0x2d80
+  __TEXT.__objc_methlist: 0xc14
+  __TEXT.__const: 0x5ee1
+  __TEXT.__gcc_except_tab: 0xcb0
+  __TEXT.__cstring: 0x68b2
+  __TEXT.__oslogstring: 0x5afc
   __TEXT.__objc_classname: 0x194
-  __TEXT.__objc_methname: 0x2c89
-  __TEXT.__objc_methtype: 0xae6
-  __TEXT.__unwind_info: 0x1088
+  __TEXT.__objc_methname: 0x2c5b
+  __TEXT.__objc_methtype: 0xaf6
+  __TEXT.__unwind_info: 0x1070
   __DATA_CONST.__auth_got: 0x11f0
-  __DATA_CONST.__got: 0x790
+  __DATA_CONST.__got: 0x7a0
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x4a38
-  __DATA_CONST.__cfstring: 0x5e20
+  __DATA_CONST.__const: 0x4a10
+  __DATA_CONST.__cfstring: 0x6000
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_intobj: 0x108
-  __DATA_CONST.__objc_arraydata: 0x40
+  __DATA_CONST.__objc_arraydata: 0xe0
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x1450
+  __DATA_CONST.__objc_dictobj: 0x190
+  __DATA.__objc_const: 0x1480
   __DATA.__objc_selrefs: 0xd10
-  __DATA.__objc_ivar: 0xb4
+  __DATA.__objc_ivar: 0xb8
   __DATA.__objc_data: 0x460
-  __DATA.__data: 0x3a8
-  __DATA.__bss: 0x4f0
+  __DATA.__data: 0x3c0
+  __DATA.__bss: 0x500
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 3DAC758D-DA0E-3E59-962C-1F055D977393
-  Functions: 1245
-  Symbols:   830
-  CStrings:  2916
+  UUID: 2443C64A-1E9D-33DC-917F-19713C747AE6
+  Functions: 1249
+  Symbols:   833
+  CStrings:  2950
 
Symbols:
+ _NSCocoaErrorDomain
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSMutableSet
CStrings:
+ "@\"NSMutableSet\""
+ "AssetSavedEvent"
+ "AssetTriggerEvent"
+ "Malformed anchor record for %{public}@, not a dictionary: %{public}@"
+ "Malformed anchor record for %{public}@, type not a string: %{public}@"
+ "Malformed anchor records for %{public}@, not an array"
+ "OTAOnAuthAPFS"
+ "OTAValidPath"
+ "RemoveOldAppleAnchorSource"
+ "RemoveOldSystemAnchorSource"
+ "Successfully locked and loaded asset version %llu"
+ "T@\"NSMutableSet\",&,V_apple_anchor_lookups"
+ "Unable to read trust store version from asset path, giving up: %@"
+ "_apple_anchor_lookups"
+ "allObjects"
+ "allowTestAnchors"
+ "apple_anchor_lookups"
+ "checkAssetVersion"
+ "com.apple.MobileAssetError.AutoAsset"
+ "com.apple.security.file./Library/Caches/com.apple.xbs/Sources/Security_executables_core/trust/trustd/OTAAutoAssetClient.m"
+ "initAutoAsset"
+ "interest"
+ "loadAppleAnchors"
+ "lockContent"
+ "no OTAAutoAssetPathKey from %{public}@"
+ "readSettings"
+ "set"
+ "setApple_anchor_lookups:"
+ "spi"
+ "test-custom"
+ "test-platform"
+ "test-system"
+ "validPath"
- "AssetBuiltInEvent"
- "Ended local asset locks for %@"
- "Failed to eliminate asset: %@"
- "Failed to end asset locks for %@: %@"
- "RootConstraints"
- "Successfully removed interest for %@"
- "Unable to read trust store version from asset path, giving up"
- "_endLocalAssetLocks"
- "_removeInterestInAssetType:withAssetSpecifier:withError:"
- "dictionaryWithContentsOfFile:"
- "eliminateAllForSelector:completion:"
- "endAllPreviousLocksOfSelector:completion:"
- "stopUsingLocalAsset"
- "unable to resolve location of %{public}@"

```
