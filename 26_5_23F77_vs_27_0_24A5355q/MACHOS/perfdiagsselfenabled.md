## perfdiagsselfenabled

> `/usr/libexec/perfdiagsselfenabled`

```diff

-398.2.0.0.0
-  __TEXT.__text: 0xce28
-  __TEXT.__auth_stubs: 0x560
-  __TEXT.__objc_stubs: 0xea0
-  __TEXT.__objc_methlist: 0xaa8
-  __TEXT.__const: 0x22c
-  __TEXT.__cstring: 0x13d8
-  __TEXT.__oslogstring: 0x202e
-  __TEXT.__objc_classname: 0xda
+412.0.0.0.0
+  __TEXT.__text: 0xc620
+  __TEXT.__auth_stubs: 0x600
+  __TEXT.__objc_stubs: 0xf40
+  __TEXT.__objc_methlist: 0xad8
+  __TEXT.__const: 0x20c
+  __TEXT.__cstring: 0x1491
+  __TEXT.__oslogstring: 0x2096
+  __TEXT.__objc_classname: 0xd2
   __TEXT.__objc_methtype: 0x553
-  __TEXT.__objc_methname: 0x332d
+  __TEXT.__objc_methname: 0x3430
   __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__unwind_info: 0x278
-  __DATA_CONST.__auth_got: 0x2c0
-  __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0x660
-  __DATA_CONST.__cfstring: 0x1580
+  __TEXT.__unwind_info: 0x270
+  __DATA_CONST.__const: 0x6c8
+  __DATA_CONST.__cfstring: 0x1680
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x1b40
-  __DATA.__objc_selrefs: 0x740
-  __DATA.__objc_ivar: 0x1bc
+  __DATA_CONST.__auth_got: 0x310
+  __DATA_CONST.__got: 0xc8
+  __DATA.__objc_const: 0x1ba0
+  __DATA.__objc_selrefs: 0x780
+  __DATA.__objc_ivar: 0x1c4
   __DATA.__objc_data: 0x370
-  __DATA.__data: 0x30
-  __DATA.__bss: 0x60
+  __DATA.__data: 0x38
+  __DATA.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 39FA4116-92B3-3D46-8B3C-EF4E6BA6E836
+  UUID: D5BA7F74-DB04-38A0-9605-4787A74C6206
   Functions: 320
-  Symbols:   118
-  CStrings:  999
+  Symbols:   130
+  CStrings:  1029
 
Symbols:
+ _NSStringFromSelector
+ _OBJC_CLASS_$_NSMutableDictionary
+ ___kCFBooleanTrue
+ __os_log_fault_impl
+ _objc_claimAutoreleasedReturnValue
+ _objc_opt_isKindOfClass
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x25
+ _objc_retain_x3
+ _objc_retain_x8
+ _object_getClassName
+ _sel_getName
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x23
CStrings:
+ "HTPrefs: %{public}@ has unexpected type %{public}s (expected selector %{public}s) with value %{public}@"
+ "HangTracerEnableHUDClients"
+ "HangTracerHUDOpacity"
+ "TB,R,V_areHUDClientsEnabled"
+ "TI,R,V_hudOpacityLevel"
+ "_areHUDClientsEnabled"
+ "_hudOpacityLevel"
+ "areHUDClientsEnabled"
+ "class_name"
+ "com.apple.da.hud_layer_refresh"
+ "com.apple.hangtracer.prefs_type_mismatch"
+ "description"
+ "dictionary"
+ "expected_selector"
+ "hudOpacityLevel"
+ "initPropertyAreHUDClientsEnabled:"
+ "initPropertyHUDOpacity:"
+ "key_name"
+ "setObject:forKeyedSubscript:"
+ "stringWithUTF8String:"
+ "type_mismatch"
+ "value"
+ "\xf0\xf0Q!f!"
- "\xf0\xf0A!f!"

```
