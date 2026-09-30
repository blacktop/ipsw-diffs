## sensorkitd

> `/usr/libexec/sensorkitd`

```diff

-860.0.6.0.0
-  __TEXT.__text: 0x40e40
-  __TEXT.__auth_stubs: 0xc40
+860.0.16.0.0
+  __TEXT.__text: 0x40f50
+  __TEXT.__auth_stubs: 0xc50
   __TEXT.__objc_stubs: 0x37a0
   __TEXT.__objc_methlist: 0x24ac
   __TEXT.__const: 0x150
   __TEXT.__objc_methname: 0x5925
   __TEXT.__objc_classname: 0x8de
   __TEXT.__objc_methtype: 0x2635
-  __TEXT.__cstring: 0x2cb5
+  __TEXT.__cstring: 0x2d64
   __TEXT.__oslogstring: 0x6abe
   __TEXT.__gcc_except_tab: 0x690
   __TEXT.__unwind_info: 0x9f0
-  __DATA_CONST.__auth_got: 0x630
+  __DATA_CONST.__auth_got: 0x638
   __DATA_CONST.__got: 0x380
-  __DATA_CONST.__const: 0xfb8
-  __DATA_CONST.__cfstring: 0x3080
+  __DATA_CONST.__const: 0xfd0
+  __DATA_CONST.__cfstring: 0x30e0
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x178

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
   Functions: 797
-  Symbols:   324
-  CStrings:  2204
+  Symbols:   325
+  CStrings:  2208
 
Symbols:
+ _os_transaction_create
CStrings:
+ "com.apple.SensorKit.soundDetection.telephony"
+ "com.apple.SensorKit.speechEmotion.telephony"
+ "com.apple.SensorKit.speechMetrics.telephony"
+ "com.apple.sensorkitd.updateAuthorizations"

```
