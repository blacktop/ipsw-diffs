## PushKit

> `/System/Library/Frameworks/PushKit.framework/Versions/A/PushKit`

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
-  __TEXT.__text: 0x5218
-  __TEXT.__auth_stubs: 0x300
+  __TEXT.__text: 0x51b8
+  __TEXT.__auth_stubs: 0x2e0
   __TEXT.__objc_methlist: 0x798
   __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0x84

   __DATA_CONST.__objc_selrefs: 0x508
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x190
+  __AUTH_CONST.__auth_got: 0x180
   __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__cfstring: 0x2e0
   __AUTH_CONST.__objc_const: 0xe28

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 180
-  Symbols:   488
+  Functions: 179
+  Symbols:   485
   CStrings:  315
 
Symbols:
- ___73-[PKPushRegistry voipPayloadReceived:mustPostCall:withCompletionHandler:]_block_invoke_4
- _dispatch_after
- _dispatch_time
Functions:
~ ___73-[PKPushRegistry voipPayloadReceived:mustPostCall:withCompletionHandler:]_block_invoke : 772 -> 684
~ __73-[PKPushRegistry voipPayloadReceived:mustPostCall:withCompletionHandler:]_block_invoke.37 : 8 -> 160
~ __73-[PKPushRegistry voipPayloadReceived:mustPostCall:withCompletionHandler:]_block_invoke_2.38 : 160 -> 164
~ ___73-[PKPushRegistry voipPayloadReceived:mustPostCall:withCompletionHandler:]_block_invoke_3 : 164 -> 16
- ___73-[PKPushRegistry voipPayloadReceived:mustPostCall:withCompletionHandler:]_block_invoke_4
```
