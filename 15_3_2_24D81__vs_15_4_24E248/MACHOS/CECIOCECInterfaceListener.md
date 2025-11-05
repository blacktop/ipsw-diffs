## CECIOCECInterfaceListener

> `/System/Library/PrivateFrameworks/CoreRC.framework/PlugIns/InterfacePlugins/CECIOCECInterfaceListener.plugin/Contents/MacOS/CECIOCECInterfaceListener`

```diff

-65.0.0.0.0
-  __TEXT.__text: 0x1474
-  __TEXT.__auth_stubs: 0x1f0
-  __TEXT.__objc_stubs: 0x400
+67.0.0.0.0
+  __TEXT.__text: 0x1720
+  __TEXT.__auth_stubs: 0x200
+  __TEXT.__objc_stubs: 0x500
   __TEXT.__objc_methlist: 0x16c
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x516
-  __TEXT.__objc_methname: 0x440
+  __TEXT.__cstring: 0x4ef
+  __TEXT.__objc_methname: 0x487
   __TEXT.__objc_classname: 0x2c
-  __TEXT.__objc_methtype: 0x169
-  __TEXT.__unwind_info: 0xb8
-  __DATA_CONST.__auth_got: 0x100
-  __DATA_CONST.__got: 0x78
+  __TEXT.__objc_methtype: 0x1ee
+  __TEXT.__unwind_info: 0xc0
+  __DATA_CONST.__auth_got: 0x108
+  __DATA_CONST.__got: 0x90
   __DATA_CONST.__const: 0x90
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA.__objc_const: 0x288
-  __DATA.__objc_selrefs: 0x160
+  __DATA.__objc_selrefs: 0x1a0
   __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/IOCEC.framework/Versions/A/IOCEC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8E8EDE4F-0990-3D50-9F23-149BD2A897DB
-  Functions: 38
-  Symbols:   59
-  CStrings:  114
+  UUID: C6A7C217-5E80-39D6-9B27-F739B4B3690A
+  Functions: 47
+  Symbols:   63
+  CStrings:  120
 
Symbols:
+ _OBJC_CLASS_$_CECEDIDAttributes
+ _OBJC_CLASS_$_NSString
+ _kCECInterfacePropertyEDIDAttributes
+ _objc_alloc_init
CStrings:
+ "%@ %s address=0x%04x, hpd=%d, hibernate=%d, vendorID=%06x, modelName=%s, uuid=%s\n"
+ "-[CECIOCECInterface _updateStatusWithEDID:HPD:hibernate:]"
+ "T{?=SSSCS[32c][37c]},N,V_attributes"
+ "_attributes"
+ "_updateStatusWithEDID:HPD:hibernate:"
+ "attributes"
+ "setAddress:"
+ "setAttributes:"
+ "setModelName:"
+ "setProductID:"
+ "setUuid:"
+ "setVendorID:"
+ "setWeek:"
+ "setYear:"
+ "stringWithCString:encoding:"
+ "v104@0:8{?=SSSCS[32c][37c]}16B96B100"
+ "v96@0:8{?=SSSCS[32c][37c]}16"
+ "{?=\"address\"S\"vendorID\"S\"productID\"S\"week\"C\"year\"S\"modelName\"[32c]\"uuid\"[37c]}"
+ "{?=SSSCS[32c][37c]}16@0:8"
- "%@ %s address=0x%04x, hpd=%d, hibernate=%d\n"
- "%s _packedPhysicalAddress=0x%02x\n"
- "-[CECIOCECInterface _updateStatusWithPhysicalAddress:HPD:hibernate:]"
- "-[CECIOCECInterface properties]"
- "S"
- "S16@0:8"
- "TS,N,V_packedPhysicalAddress"
- "_packedPhysicalAddress"
- "_updateStatusWithPhysicalAddress:HPD:hibernate:"
- "packedPhysicalAddress"
- "setPackedPhysicalAddress:"
- "v20@0:8S16"
- "v28@0:8S16B20B24"

```
