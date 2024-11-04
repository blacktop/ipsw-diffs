## dockaccessoryd

> `/usr/libexec/dockaccessoryd`

```diff

-251.2.0.0.0
-  __TEXT.__text: 0x1f86f0
+260.0.0.0.0
+  __TEXT.__text: 0x1fa7e4
   __TEXT.__auth_stubs: 0x35e0
-  __TEXT.__objc_stubs: 0xc1e0
+  __TEXT.__objc_stubs: 0xc200
   __TEXT.__objc_methlist: 0x9100
-  __TEXT.__objc_methname: 0x15cb8
-  __TEXT.__cstring: 0xc525
+  __TEXT.__objc_methname: 0x15cd2
+  __TEXT.__cstring: 0xc845
   __TEXT.__objc_classname: 0x14a3
   __TEXT.__objc_methtype: 0x3484
-  __TEXT.__const: 0x39b8
-  __TEXT.__oslogstring: 0x14492
+  __TEXT.__const: 0x3a08
+  __TEXT.__oslogstring: 0x1464d
   __TEXT.__gcc_except_tab: 0xd4c
-  __TEXT.__swift5_typeref: 0x2552
+  __TEXT.__swift5_typeref: 0x256c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x4e00
+  __TEXT.__constg_swiftt: 0x4e38
   __TEXT.__swift5_builtin: 0x1e0
-  __TEXT.__swift5_reflstr: 0x219a
-  __TEXT.__swift5_fieldmd: 0x24f4
+  __TEXT.__swift5_reflstr: 0x21ca
+  __TEXT.__swift5_fieldmd: 0x255c
   __TEXT.__swift5_assocty: 0x270
   __TEXT.__swift5_capture: 0x1410
   __TEXT.__swift5_proto: 0x21c
-  __TEXT.__swift5_types: 0x1f0
+  __TEXT.__swift5_types: 0x1f8
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x4ce8
+  __TEXT.__unwind_info: 0x4d18
   __TEXT.__eh_frame: 0x5178
   __DATA_CONST.__auth_got: 0x1b00
   __DATA_CONST.__got: 0xba8
-  __DATA_CONST.__auth_ptr: 0x878
-  __DATA_CONST.__const: 0x7a08
+  __DATA_CONST.__auth_ptr: 0x918
+  __DATA_CONST.__const: 0x7ab8
   __DATA_CONST.__cfstring: 0x5be0
   __DATA_CONST.__objc_classlist: 0x638
   __DATA_CONST.__objc_catlist: 0x18

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x17608
-  __DATA.__objc_selrefs: 0x4230
+  __DATA.__objc_selrefs: 0x4238
   __DATA.__objc_ivar: 0xa04
   __DATA.__objc_data: 0x6fa0
   __DATA.__data: 0x6420

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 6755
-  Symbols:   1395
-  CStrings:  7046
+  Functions: 6781
+  Symbols:   1396
+  CStrings:  7059
 
Symbols:
+ _$sytWV
CStrings:
+ "12345678-AAAA-BBBB-CCCC-01234567890F"
+ "<?xml version=\"1.0\" ?>\n\n<mock_stand name=\"noop_stand\" manufacturer=\"noop\" version=\"0\">\n\t<motion_controller model=\"YPR\" name=\"tracking\">\n\t\t<yaw type=\"revolute\" id=\"0\">\n\t\t\t<limits home=\"0.0\" velocity=\"1.2\" acceleration=\"8.0\" lower=\"-1.74\" upper=\"1.74\"/>\n\t\t\t<control kp=\"0.0\" ki=\"0.0\" kd=\"0.0\" kv=\"0.0\" i_max=\"0.0\"/>\n\t\t</yaw>\n\t\t<pitch type=\"revolute\" id=\"1\">\n\t\t\t<limits home=\"0.0\" velocity=\"1.2\" acceleration=\"8.0\" lower=\"-1.22\" upper=\"1.22\" />\n\t\t\t<control kp=\"0.0\" ki=\"0.0\" kd=\"0.0\" kv=\"0.0\" i_max=\"0.0\"/>\n\t\t</pitch>\n\t</motion_controller>\n\n\t<!-- components -->\n\t<sensor_controller name=\"sensors\">\n\t\t<button id=\"3\" name=\"trackingEnable\" />\n\t\t<led id=\"4\" name=\"trackingActive\"/>\n\t\t<battery id=\"5\" name=\"mainBattery\"/>\n\t</sensor_controller>\n</mock_stand>"
+ "Failed parsing mock accessorys: %!@(MISSING)"
+ "Failed retrieving mock accessory"
+ "Mock device - not scanning, immediately marking as connected"
+ "Tearing down debug accessory for %!s(MISSING)"
+ "adding debug mock"
+ "getActuatorFeedback: noop for mock device"
+ "initWithOptions:capacity:"
+ "mock stand"
+ "setActuatorPositions: noop for mock device"
+ "setActuatorVelocities: noop for mock device"
+ "stopActuatorFeedback: noop for mock device"

```
