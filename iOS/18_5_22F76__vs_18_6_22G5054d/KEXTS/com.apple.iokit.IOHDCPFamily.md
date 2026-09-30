## com.apple.iokit.IOHDCPFamily

> `com.apple.iokit.IOHDCPFamily`

```diff

-68.0.0.0.0
+70.0.0.0.0
   __TEXT.__const: 0x38
-  __TEXT.__cstring: 0x435d
+  __TEXT.__cstring: 0x437d
   __TEXT.__os_log: 0x1626
-  __TEXT_EXEC.__text: 0xf364
+  __TEXT_EXEC.__text: 0xf39c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x178

   __DATA_CONST.__mod_term_func: 0x48
   __DATA_CONST.__const: 0x1c10
   __DATA_CONST.__kalloc_type: 0x340
-  UUID: 7AC9FD3C-4EED-3E21-9FEB-4E08559F0CB3
+  UUID: 27DCDC3A-F1BD-3CDE-8F04-D91B05242A90
   Functions: 382
   Symbols:   0
-  CStrings:  557
+  CStrings:  558
 
Functions:
~ sub_fffffff00a19f798 -> sub_fffffff00a241f88 : 244 -> 252
~ __ZN29IOHDCP2TransmitterAuthSession13handleMessageEP14IOHDCP2Message : 5188 -> 5196
~ __ZN31IOHDCP2DPTransmitterAuthSession30fillRepeaterAuth_Stream_ManageEPN14IOHDCP2Message29DP_RepeaterAuth_Stream_ManageE : 420 -> 424
~ __ZN31IOHDCP2DPTransmitterAuthSession13handleMessageEP14IOHDCP2Message : 4212 -> 4248
CStrings:
+ "12111211111211122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
+ "ret = setTimeoutMS(110) == 0 "
+ "ret = setTimeoutMS(16) == 0 "
- "1211121111121112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
- "ret = setTimeoutMS(7) == 0 "

```
