## CFAccountPolicy

> `/System/Library/PrivateFrameworks/AccountPolicy.framework/Frameworks/CFAccountPolicy.framework/Versions/A/CFAccountPolicy`

```diff

-61.0.0.0.0
-  __TEXT.__text: 0x1504
+62.0.0.0.0
+  __TEXT.__text: 0x14d4
   __TEXT.__auth_stubs: 0xe0
   __TEXT.__cstring: 0xa6a
   __TEXT.__const: 0x10
-  __TEXT.__unwind_info: 0xc8
+  __TEXT.__unwind_info: 0xd0
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0x1e8
   __AUTH_CONST.__auth_got: 0x70

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1628DF2C-AB7A-3AFC-AF0E-FAC100A4D483
-  Functions: 46
-  Symbols:   128
+  UUID: 7EEC860D-B98E-3438-B53D-5FEA9BFC53E5
+  Functions: 48
+  Symbols:   134
   CStrings:  144
 
Symbols:
+ APPolicyGetTypeID.cold.1
+ APPolicySetGetTypeID.cold.1
+ _APPolicyCreate.cold.1
+ _APPolicySetCreate.cold.1
+ _isValidAPPolicy.cold.1
+ _isValidAPPolicySet.cold.1
Functions:
~ _APPolicyGetTypeID : 68 -> 56
~ __APPolicyCreate : 108 -> 92
~ __isValidAPPolicy : 148 -> 132
~ _APPolicySetGetTypeID : 68 -> 56
~ __APPolicySetCreate : 108 -> 92
~ __isValidAPPolicySet : 148 -> 132

```
