## tvremoted

> `/usr/libexec/tvremoted`

```diff

-367.0.9.0.0
-  __TEXT.__text: 0xc858
+367.10.21.0.0
+  __TEXT.__text: 0xcdd4
   __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_stubs: 0x1f60
-  __TEXT.__objc_methlist: 0x8e8
+  __TEXT.__objc_stubs: 0x2020
+  __TEXT.__objc_methlist: 0x8f4
   __TEXT.__const: 0x7a
-  __TEXT.__oslogstring: 0x19fa
-  __TEXT.__cstring: 0x6f9
-  __TEXT.__gcc_except_tab: 0x16c
-  __TEXT.__objc_methname: 0x2a67
+  __TEXT.__oslogstring: 0x1afe
+  __TEXT.__cstring: 0x73e
+  __TEXT.__gcc_except_tab: 0x180
+  __TEXT.__objc_methname: 0x2ae7
   __TEXT.__objc_classname: 0x14a
   __TEXT.__objc_methtype: 0xb5e
   __TEXT.__unwind_info: 0x2e8
   __DATA_CONST.__auth_got: 0x288
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x660
-  __DATA_CONST.__cfstring: 0x540
+  __DATA_CONST.__cfstring: 0x560
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x30
   __DATA.__objc_const: 0x15d8
-  __DATA.__objc_selrefs: 0xa40
-  __DATA.__objc_classrefs: 0x180
+  __DATA.__objc_selrefs: 0xa70
+  __DATA.__objc_classrefs: 0x188
   __DATA.__objc_superrefs: 0x20
   __DATA.__objc_ivar: 0x7c
   __DATA.__objc_data: 0x190

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 5CEBE977-CEA0-3D53-B22F-0649340DCA01
-  Functions: 266
-  Symbols:   2122
-  CStrings:  803
+  UUID: 3EA59327-BC42-3DED-A0DF-B990DF11B746
+  Functions: 272
+  Symbols:   2159
+  CStrings:  817
 
Symbols:
+ -[TVRDServer _updateDevicesWithRecommendations:]
+ -[TVRDServer _updateDevicesWithRecommendations:].cold.1
+ -[TVRDServer _updateDevicesWithRecommendations:].cold.2
+ -[TVRDServer _updateDevicesWithRecommendations:].cold.3
+ _OBJC_CLASS_$_NSPredicate
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _objc_msgSend$_updateDevicesWithRecommendations:
+ _objc_msgSend$anyObject
+ _objc_msgSend$conciseDescription
+ _objc_msgSend$filteredSetUsingPredicate:
+ _objc_msgSend$intersectSet:
+ _objc_msgSend$predicateWithFormat:
CStrings:
+ "%@ is already interested in identifier %{public}@. All interested IDs - %@"
+ "-[TVRDServer _updateDevicesWithRecommendations:]"
+ "Assigning classification from suggestedDevice: %{public}@ to device: %{public}@"
+ "Close connection to device %{public}@ with type %ld"
+ "Open connection to device %{public}@"
+ "Queried devices subset: %@"
+ "Queried devices: %@"
+ "Suggested devices: %{public}@"
+ "There are no suggested devices. Skipping updating devices with recommendations"
+ "_updateDevicesWithRecommendations:"
+ "anyObject"
+ "conciseDescription"
+ "filteredSetUsingPredicate:"
+ "identifier ==[c] %@"
+ "intersectSet:"
+ "predicateWithFormat:"
- "%@ is already interested in identifier %@. All interested IDs - %@"
- "Close connection to device %@ with type %ld"
- "Open connection to device %@"

```
