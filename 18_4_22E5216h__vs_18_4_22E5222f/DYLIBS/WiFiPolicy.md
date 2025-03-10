## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

```diff

-980.34.0.0.0
-  __TEXT.__text: 0xb8b28
+980.36.0.0.0
+  __TEXT.__text: 0xb8fc8
   __TEXT.__auth_stubs: 0x15f0
-  __TEXT.__objc_methlist: 0x110b8
+  __TEXT.__objc_methlist: 0x110c0
   __TEXT.__const: 0x638
-  __TEXT.__cstring: 0x1bf6f
-  __TEXT.__oslogstring: 0x3a15
+  __TEXT.__cstring: 0x1bfff
+  __TEXT.__oslogstring: 0x3abf
   __TEXT.__gcc_except_tab: 0x18f0
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__unwind_info: 0x2188
-  __TEXT.__objc_classname: 0x1379
-  __TEXT.__objc_methname: 0x31869
+  __TEXT.__objc_classname: 0x137a
+  __TEXT.__objc_methname: 0x318fe
   __TEXT.__objc_methtype: 0x3a26
   __TEXT.__objc_stubs: 0x180a0
   __DATA_CONST.__got: 0xa40

   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9740
+  __DATA_CONST.__objc_selrefs: 0x9748
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x430
   __DATA_CONST.__objc_arraydata: 0xa58

   __AUTH_CONST.__auth_ptr: 0x20
   __AUTH_CONST.__const: 0x3e0
   __AUTH_CONST.__cfstring: 0x18780
-  __AUTH_CONST.__objc_const: 0x20a28
+  __AUTH_CONST.__objc_const: 0x20ad8
   __AUTH_CONST.__objc_intobj: 0x1740
   __AUTH_CONST.__objc_arrayobj: 0x390
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x820
-  __DATA.__objc_ivar: 0x2080
+  __DATA.__objc_ivar: 0x2094
   __DATA.__data: 0x1bc0
   __DATA.__bss: 0x22
   __DATA_DIRTY.__objc_data: 0x2a80

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6009
-  Symbols:   7013
-  CStrings:  13204
+  Functions: 6011
+  Symbols:   7015
+  CStrings:  13216
 
CStrings:
+ "\x12\x12B!\x11"
+ "%s on %@ deferCompletion=%s"
+ "%s: %s joining %@, seqNo %d, reason %@, failure %d"
+ "%s: link session completion deferred for %{private}@, deferred count %d"
+ "%s: link session ended for %{private}@, deferred count %d"
+ "-[WiFiUsageLinkSession joinStateDidChange:withReason:lastDisconnectReason:lastJoinFailure:andNetworkDetails:]"
+ "-[WiFiUsageSession sessionDidEnd]"
+ "TB,N,V_deferCompletion"
+ "_deferCompletion"
+ "_deferredFailureSessions"
+ "_joinAttemptedBeforeLinkDown"
+ "_joinSeqNo"
+ "_lastSubmittedSessionSeqNo"
+ "deferCompletion"
+ "setDeferCompletion:"
- "\x12\x12B!"
- "%s: link session ended for %{private}@"
- "summarizeBandUsage"

```
