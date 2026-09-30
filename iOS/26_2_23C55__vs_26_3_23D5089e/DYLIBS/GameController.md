## GameController

> `/System/Library/Frameworks/GameController.framework/GameController`

```diff

-13.2.8.0.0
-  __TEXT.__text: 0x10716c
+13.3.1.0.0
+  __TEXT.__text: 0x107638
   __TEXT.__auth_stubs: 0x1c30
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xff0c
+  __TEXT.__objc_methlist: 0xff2c
   __TEXT.__const: 0x3d44
-  __TEXT.__cstring: 0xa279
+  __TEXT.__cstring: 0xa419
   __TEXT.__gcc_except_tab: 0x59ec
   __TEXT.__oslogstring: 0x97d8
   __TEXT.__dlopen_cstrs: 0xfd

   __TEXT.__swift5_types: 0x60
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_capture: 0xc4
-  __TEXT.__unwind_info: 0x53e8
+  __TEXT.__unwind_info: 0x5400
   __TEXT.__eh_frame: 0xf8
   __TEXT.__objc_classname: 0x41b3
   __TEXT.__objc_methname: 0x1920b
   __TEXT.__objc_methtype: 0x7bdd
-  __TEXT.__objc_stubs: 0xf600
+  __TEXT.__objc_stubs: 0xf640
   __DATA_CONST.__got: 0xba8
   __DATA_CONST.__const: 0x2db0
   __DATA_CONST.__objc_classlist: 0x990

   __DATA_CONST.__objc_superrefs: 0x8c8
   __DATA_CONST.__objc_arraydata: 0x570
   __AUTH_CONST.__auth_got: 0xe30
-  __AUTH_CONST.__const: 0x1f98
-  __AUTH_CONST.__cfstring: 0xb800
+  __AUTH_CONST.__const: 0x1fb8
+  __AUTH_CONST.__cfstring: 0xb8c0
   __AUTH_CONST.__objc_const: 0x49440
   __AUTH_CONST.__objc_intobj: 0x14a0
   __AUTH_CONST.__objc_dictobj: 0xa0

   __DATA.__objc_ivar: 0x17bc
   __DATA.__data: 0x5e10
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x1f10
+  __DATA.__bss: 0x1f20
   __DATA.__common: 0x78
   __DATA_DIRTY.__objc_data: 0x1130
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 7DF67129-F00A-394C-8F5A-5FD7F91C8565
-  Functions: 7404
-  Symbols:   27503
-  CStrings:  9859
+  UUID: 91F21065-FD1C-334B-B171-C6DBCB9311C9
+  Functions: 7407
+  Symbols:   27513
+  CStrings:  9871
 
Symbols:
+ -[_GCDevicePhysicalInputButtonElementParameters debugDescription]
+ -[_GCDevicePhysicalInputElementParameters debugDescription]
+ __MergedGlobals
+ ___42-[_GCDevicePhysicalInputSensorInput value]_block_invoke
+ _objc_msgSend$forceInput
+ _objc_msgSend$scaledValue
Functions:
~ +[_GCSonyPSVR2SenseControllerProfile logicalDevice:makeControllerInputDescriptionWithIdentifier:bindings:forClient:] : 6436 -> 6400
+ ___42-[_GCDevicePhysicalInputSensorInput value]_block_invoke
+ -[_GCDevicePhysicalInputElementParameters debugDescription]
~ -[_GCDevicePhysicalInputButtonElement description] : 236 -> 860
+ -[_GCDevicePhysicalInputButtonElementParameters debugDescription]
~ -[_GCDevicePhysicalInputSensorInput value] : 56 -> 132
CStrings:
+ "%@\n\t sources: %@\n\t analog: %d\n\t pressedThreshold: %f\n\t eventPressedValueField: %zd\n\t eventAnalogPressValueField: %zd\n\t eventTouchValueField: %zd\n\t eventForceValueField: %zd\n\t touch: %@\n\t force: %@"
+ "%@, analog: %s, press = %f%@, force = %f (%f)"
+ "%@, analog: %s, press = %f%@, touch = %@"
+ "%@, analog: %s, press = %f%@, touch = %@, force = %f (%f)"
+ "(not touched)"
+ "<%@ %p> '%@'\n\t aliases: %@\n\t localizedName: %@\n\t symbol: %@"

```
