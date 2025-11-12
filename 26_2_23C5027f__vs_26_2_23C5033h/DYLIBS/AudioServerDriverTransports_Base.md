## AudioServerDriverTransports_Base

> `/System/Library/PrivateFrameworks/AudioServerDriverTransports_Base.framework/AudioServerDriverTransports_Base`

```diff

-320.1.0.0.0
-  __TEXT.__text: 0x3ff74
-  __TEXT.__auth_stubs: 0xe60
-  __TEXT.__objc_methlist: 0x3404
-  __TEXT.__gcc_except_tab: 0x63f8
+320.2.0.0.0
+  __TEXT.__text: 0x4041c
+  __TEXT.__auth_stubs: 0xea0
+  __TEXT.__objc_methlist: 0x3454
+  __TEXT.__gcc_except_tab: 0x63ec
   __TEXT.__const: 0x50e
-  __TEXT.__cstring: 0x1412
-  __TEXT.__oslogstring: 0x2fff
-  __TEXT.__unwind_info: 0x2010
-  __TEXT.__objc_classname: 0x6a1
-  __TEXT.__objc_methname: 0x6ea1
-  __TEXT.__objc_methtype: 0x1013
-  __TEXT.__objc_stubs: 0x6560
+  __TEXT.__cstring: 0x1424
+  __TEXT.__oslogstring: 0x3021
+  __TEXT.__unwind_info: 0x2028
+  __TEXT.__objc_classname: 0x6ae
+  __TEXT.__objc_methname: 0x6edf
+  __TEXT.__objc_methtype: 0x1036
+  __TEXT.__objc_stubs: 0x65e0
   __DATA_CONST.__got: 0x2b8
-  __DATA_CONST.__const: 0x760
-  __DATA_CONST.__objc_classlist: 0x198
+  __DATA_CONST.__const: 0x780
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ce0
+  __DATA_CONST.__objc_selrefs: 0x1d08
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x168
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x748
+  __AUTH_CONST.__auth_got: 0x768
   __AUTH_CONST.__const: 0x450
-  __AUTH_CONST.__cfstring: 0x1900
-  __AUTH_CONST.__objc_const: 0x5200
+  __AUTH_CONST.__cfstring: 0x1940
+  __AUTH_CONST.__objc_const: 0x5290
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x910
+  __AUTH.__objc_data: 0x960
   __DATA.__objc_ivar: 0x318
   __DATA.__data: 0x840
-  __DATA.__bss: 0x48
+  __DATA.__bss: 0x58
   __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x40

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 67B17861-BE06-33A4-984B-491A88DBAB29
-  Functions: 1683
-  Symbols:   5703
-  CStrings:  2302
+  UUID: 3AD704D5-07E9-3284-AE66-4C32BF854A09
+  Functions: 1691
+  Symbols:   5735
+  CStrings:  2315
 
Symbols:
+ +[ASDTBootArgs getBool:]
+ +[ASDTBootArgs getString:]
+ +[ASDTBootArgs getUInt64:]
+ +[ASDTBootArgs get]
+ +[ASDTBootArgs initBootArgsFrom:]
+ +[ASDTBootArgs initBootArgs]
+ +[ASDTBootArgs initBootArgs].cold.1
+ _OBJC_CLASS_$_ASDTBootArgs
+ _OBJC_METACLASS_$_ASDTBootArgs
+ __OBJC_$_CLASS_METHODS_ASDTBootArgs
+ __OBJC_CLASS_RO_$_ASDTBootArgs
+ __OBJC_METACLASS_RO_$_ASDTBootArgs
+ ___19+[ASDTBootArgs get]_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ ___error
+ _gBootArgs
+ _get.onceToken
+ _objc_msgSend$getString:
+ _objc_msgSend$getUInt64:
+ _objc_msgSend$initBootArgs
+ _objc_msgSend$initBootArgsFrom:
+ _strerror
+ _strtoull
+ _sysctlbyname
CStrings:
+ " "
+ "320.2"
+ "="
+ "ASDTBootArgs"
+ "Failed to load boot args: [%d] %s"
+ "Q24@0:8@16"
+ "getBool:"
+ "getString:"
+ "getUInt64:"
+ "initBootArgs"
+ "initBootArgsFrom:"
+ "kern.bootargs"
+ "{unique_ptr<ASDT::Exclaves::AudioBuffer, std::default_delete<ASDT::Exclaves::AudioBuffer>>=\"\"{?=\"__ptr_\"^{AudioBuffer}}}"
+ "{unique_ptr<ASDT::Exclaves::InboundBuffer, std::default_delete<ASDT::Exclaves::InboundBuffer>>=\"\"{?=\"__ptr_\"^{InboundBuffer}}}"
+ "{unique_ptr<ASDT::Exclaves::Sensor, std::default_delete<ASDT::Exclaves::Sensor>>=\"\"{?=\"__ptr_\"^{Sensor}}}"
+ "{unique_ptr<ASDT::Ramper, std::default_delete<ASDT::Ramper>>=\"\"{?=\"__ptr_\"^{Ramper}}}"
- "320.1"
- "{unique_ptr<ASDT::Exclaves::AudioBuffer, std::default_delete<ASDT::Exclaves::AudioBuffer>>=\"__ptr_\"^{AudioBuffer}}"
- "{unique_ptr<ASDT::Exclaves::InboundBuffer, std::default_delete<ASDT::Exclaves::InboundBuffer>>=\"__ptr_\"^{InboundBuffer}}"
- "{unique_ptr<ASDT::Exclaves::Sensor, std::default_delete<ASDT::Exclaves::Sensor>>=\"__ptr_\"^{Sensor}}"
- "{unique_ptr<ASDT::Ramper, std::default_delete<ASDT::Ramper>>=\"__ptr_\"^{Ramper}}"

```
