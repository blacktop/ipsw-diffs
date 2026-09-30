## PushKit

> `/System/Library/Frameworks/PushKit.framework/PushKit`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

 109.500.11.0.0
-  __TEXT.__text: 0x4d44
-  __TEXT.__auth_stubs: 0x420
+  __TEXT.__text: 0x4ce4
+  __TEXT.__auth_stubs: 0x400
   __TEXT.__objc_methlist: 0x798
   __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0x84

   __DATA_CONST.__objc_selrefs: 0x510
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x220
+  __AUTH_CONST.__auth_got: 0x210
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x3a0
   __AUTH_CONST.__objc_const: 0xe28

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 162
-  Symbols:   493
+  Functions: 161
+  Symbols:   490
   CStrings:  323
 
Symbols:
- ___73-[PKPushRegistry voipPayloadReceived:mustPostCall:withCompletionHandler:]_block_invoke_7
- _dispatch_after
- _dispatch_time
Functions:
~ ___73-[PKPushRegistry voipPayloadReceived:mustPostCall:withCompletionHandler:]_block_invoke : 820 -> 732
~ ___73-[PKPushRegistry voipPayloadReceived:mustPostCall:withCompletionHandler:]_block_invoke_3 : 8 -> 144
~ ___73-[PKPushRegistry voipPayloadReceived:mustPostCall:withCompletionHandler:]_block_invoke_4 : 144 -> 160
~ ___73-[PKPushRegistry voipPayloadReceived:mustPostCall:withCompletionHandler:]_block_invoke_5 : 160 -> 16
~ ___73-[PKPushRegistry voipPayloadReceived:mustPostCall:withCompletionHandler:]_block_invoke_6 : 16 -> 8
- ___73-[PKPushRegistry voipPayloadReceived:mustPostCall:withCompletionHandler:]_block_invoke_7
```
