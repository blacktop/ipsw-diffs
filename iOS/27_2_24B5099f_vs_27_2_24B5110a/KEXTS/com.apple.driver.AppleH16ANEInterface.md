## com.apple.driver.AppleH16ANEInterface

> `com.apple.driver.AppleH16ANEInterface`

```diff

-10.102.3.0.0
+10.102.4.0.0
   __TEXT.__cstring: 0x11ec2
-  __TEXT.__os_log: 0x3e23b
+  __TEXT.__os_log: 0x3e239
   __TEXT.__const: 0x1260
-  __TEXT_EXEC.__text: 0x154dd8
+  __TEXT_EXEC.__text: 0x154e1c
   __TEXT_EXEC.__auth_stubs: 0x12a0
   __DATA.__data: 0x54f4
   __DATA.__common: 0x7e0
Functions:
~ sub_fffffe0008e5457c -> sub_fffffe0008e565ec : 240 -> 244
~ __ZN11ANEResource6createIL15ANEResourceType4EEENSt3__110shared_ptrIS_EEP14ANEHWInterfaceRK25ANEResourceCreationParamsPK21ANEThreadNameRegistry : 1000 -> 1008
~ __ZNK11ANEResource10readAdviseEv : 988 -> 1020
~ __ZNK11ANEResource10createCopyEv : 440 -> 460
~ __ZN11ANEResource5_wireEj : 460 -> 464
CStrings:
+ "%s: %s: read advise vnode: %p fileOffset: %lld fileSize: 0x%llx\n"
+ "[ERROR] %s: %s: vnode read advise failed, ret=%d\n"
- "%s: %s: vnode_rdadvise vnode: %p fileOffset: %lld fileSize: 0x%llx\n"
- "[INFO] %s: %s: vnode read advise failed, ret=%d\n"
```
