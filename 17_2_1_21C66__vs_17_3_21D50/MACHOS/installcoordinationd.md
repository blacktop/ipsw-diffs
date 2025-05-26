## installcoordinationd

> `/System/Library/PrivateFrameworks/InstallCoordination.framework/Support/installcoordinationd`

```diff

-554.40.9.0.0
-  __TEXT.__text: 0x81228
+554.80.2.0.0
+  __TEXT.__text: 0x8384c
   __TEXT.__auth_stubs: 0xef0
-  __TEXT.__objc_stubs: 0x8b20
-  __TEXT.__objc_methlist: 0x411c
+  __TEXT.__objc_stubs: 0x8ca0
+  __TEXT.__objc_methlist: 0x426c
   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x134f3
-  __TEXT.__objc_classname: 0x83d
-  __TEXT.__objc_methname: 0xda7e
-  __TEXT.__oslogstring: 0xaee8
-  __TEXT.__objc_methtype: 0x1e4f
-  __TEXT.__gcc_except_tab: 0x1b10
+  __TEXT.__cstring: 0x13781
+  __TEXT.__objc_classname: 0x84e
+  __TEXT.__objc_methname: 0xdc3e
+  __TEXT.__oslogstring: 0xb34c
+  __TEXT.__objc_methtype: 0x1eae
+  __TEXT.__gcc_except_tab: 0x1b20
   __TEXT.__ustring: 0x26c
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0x1df4
+  __TEXT.__unwind_info: 0x1e50
   __DATA_CONST.__auth_got: 0x788
   __DATA_CONST.__got: 0x1a8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x23b0
-  __DATA_CONST.__cfstring: 0x7440
-  __DATA_CONST.__objc_classlist: 0x1d8
+  __DATA_CONST.__const: 0x2408
+  __DATA_CONST.__cfstring: 0x7580
+  __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x108
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0xb6a0
-  __DATA.__objc_selrefs: 0x28d8
+  __DATA.__objc_const: 0xb9f0
+  __DATA.__objc_selrefs: 0x2940
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x388
-  __DATA.__objc_superrefs: 0x188
-  __DATA.__objc_ivar: 0x3cc
-  __DATA.__objc_data: 0x1270
+  __DATA.__objc_classrefs: 0x390
+  __DATA.__objc_superrefs: 0x190
+  __DATA.__objc_ivar: 0x3d8
+  __DATA.__objc_data: 0x12c0
   __DATA.__data: 0x590
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x1c8
+  __DATA.__bss: 0x1d0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2744
+  Functions: 2788
   Symbols:   367
-  CStrings:  4462
+  CStrings:  4517
 
CStrings:
+ "%s: Client %@ is missing %@ entitlement, rejecting attempt to read app removability data. : %@"
+ "%s: Deserialized key for removability entry is not string %@ : %@"
+ "%s: Deserialized removability plist is missing key %@"
+ "%s: Deserialized removability plist is missing key %@ : %@"
+ "%s: Deserialized removability plist is not dictionary"
+ "%s: Failed to convert app removability and change clock to data : %@"
+ "%s: Failed to create dictionary from deserialized removability data: %@"
+ "%s: Failed to deserialize removability data: %@"
+ "%s: Failed to deserialize removability plist: %@"
+ "%s: Failed to extract change clock from deserialized removability plist: %@"
+ "%s: Failed to extract removability entries from deserialized removability plist: %@"
+ "%s: Failed to fetch removability metadata from %@"
+ "%s: Failed to migrate legacy removability plist to the new format with change clock: %@"
+ "%s: Failed to remove legacy removability plist at URL path %@. Error: %@"
+ "%s: Failed to write empty removability file with change clock: %@"
+ "%s: Querying removability data for client %@"
+ "%s: Received non dictionary object for %@ : %@"
+ "%s: Received non dictionary object for change clock in deserialized removability plist: %@"
+ "%s: Received non dictionary object for removability entries in deserialized removability plist: %@"
+ "%s: Received non dictionary object for requested keys %@ : %@"
+ "%s: Successfully migrated legacy removability plist to the new format with change clock"
+ "%s: Unexpectedly received nil value for app removability data : %@"
+ "-[IXSAppRemovabilityManager _onQueue_handleStateChangeForIdentity:updatedRemovability:]"
+ "-[IXSAppRemovabilityManager _onQueue_removeLegacyRemovabilityFiles]"
+ "-[IXSClientConnection _remote_removabilityDataWithCompletion:]"
+ "18:56:55"
+ "<%@ guid:%@ serialNumber:%llu>"
+ "@\"IXDataStoreClock\""
+ "@32@0:8@16Q24"
+ "Client %@ is missing %@ entitlement, rejecting attempt to read app removability data."
+ "ClockedRemovabilityMetadata.plist"
+ "Dec 20 2023"
+ "Failed to convert app removability and change clock to data"
+ "IXCopyRemovabilityStorageWithoutChangeClockURL"
+ "IXCopySerializedAppRemovabilityDataWithoutChangeClock"
+ "IXDataStoreClock"
+ "IXGetUncachedRemovabilityDataStore"
+ "RemovabilityChangeClock"
+ "RemovabilityEntries"
+ "RemovabilityStoreClock"
+ "RemovabilityVal"
+ "T@\"IXDataStoreClock\",&,N,V_removabilityChangeClock"
+ "T@\"NSUUID\",&,N,V_guid"
+ "TQ,N,V_sequenceNumber"
+ "Unexpectedly received nil value for app removability data"
+ "_ExtractObjectsFromDeserializedRemovabilityPlist"
+ "_guid"
+ "_onQueue_handleStateChangeForIdentity:updatedRemovability:"
+ "_onQueue_removeLegacyRemovabilityFiles"
+ "_remote_removabilityDataWithCompletion:"
+ "_removabilityChangeClock"
+ "_sequenceNumber"
+ "guid"
+ "increment"
+ "initWithGUID:sequenceNumber:"
+ "newClock"
+ "newClockWithDictionary:"
+ "notificationDictionary"
+ "removabilityChangeClock"
+ "removabilityDataWithChangeClock:"
+ "sequenceNumber"
+ "setGuid:"
+ "setRemovabilityChangeClock:"
+ "setSequenceNumber:"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"IXDataStoreClock\"@\"NSError\">16"
- "%s: Failed to convert app removability dictionary to data : %@"
- "%s: Failed to create dictionary from removability data: %@"
- "%s: Failed to migrate legacy removability plist to the new format: %@"
- "%s: Failed to remove legacy removability plist at URL %@. Error: %@"
- "%s: Failed to write empty removability file: %@"
- "%s: Successfully migrated legacy removability plist to the new format"
- "-[IXSAppRemovabilityManager _onQueue_handleStateChangeForIdentity:]"
- "08:00:57"
- "Failed to convert app removability dictionary to data"
- "Nov 12 2023"
- "_onQueue_handleStateChangeForIdentity:"
- "legacyRemovabilityURL"

```
