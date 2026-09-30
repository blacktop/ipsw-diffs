## com.apple.iokit.IOUserEthernet

> `com.apple.iokit.IOUserEthernet`

```diff

-79.0.0.0.0
+81.0.0.0.0
   __TEXT.__const: 0x18
   __TEXT.__cstring: 0xc71
-  __TEXT_EXEC.__text: 0x5780
+  __TEXT_EXEC.__text: 0x5814
   __TEXT_EXEC.__auth_stubs: 0x4e0
   __DATA.__data: 0xc8
   __DATA.__common: 0xb8

   __DATA_CONST.__kalloc_type: 0x180
   __DATA_CONST.__auth_got: 0x270
   __DATA_CONST.__got: 0x80
-  Functions: 166
-  Symbols:   810
+  Functions: 167
+  Symbols:   811
   CStrings:  124
 
Symbols:
+ __ZN24IOUserEthernetController17detachClientGatedEv
Functions:
~ __ZN24IOUserEthernetController18handleClientAttachEP9en_client : 888 -> 912
~ __ZN24IOUserEthernetController18handleClientDetachEP9en_client : 648 -> 552
+ __ZN24IOUserEthernetController17detachClientGatedEv
```
