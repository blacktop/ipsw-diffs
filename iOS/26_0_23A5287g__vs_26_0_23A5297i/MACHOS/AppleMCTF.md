## AppleMCTF

> `/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF`

```diff

-904.33.0.0.0
-  __TEXT.__text: 0x73a84
-  __TEXT.__auth_stubs: 0xd30
+904.58.0.0.0
+  __TEXT.__text: 0x74130
+  __TEXT.__auth_stubs: 0xd40
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x4
-  __TEXT.__gcc_except_tab: 0x648
-  __TEXT.__cstring: 0x22cb1
-  __TEXT.__const: 0x1e778
+  __TEXT.__gcc_except_tab: 0x63c
+  __TEXT.__cstring: 0x22e02
+  __TEXT.__const: 0x1e768
   __TEXT.__objc_methname: 0xb
   __TEXT.__unwind_info: 0x600
-  __DATA_CONST.__auth_got: 0x6a8
+  __DATA_CONST.__auth_got: 0x6b0
   __DATA_CONST.__got: 0x438
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x4120
+  __DATA_CONST.__const: 0x41b0
   __DATA_CONST.__cfstring: 0x2a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 96DF29CF-400E-3AA9-BB18-5636A4C340DB
-  Functions: 612
-  Symbols:   353
+  UUID: F5B3C96C-49A2-3156-A280-872C695EC0A3
+  Functions: 609
+  Symbols:   354
   CStrings:  2935
 
Symbols:
+ _CFGetRetainCount
CStrings:
+ "%lld %d AVE %s: %s:%d %s | OF: %s: MVCostBuffer is NULL"
+ "%lld %d AVE %s: %s:%d %s | OF: %s: MVCostBuffer is NULL\n"
+ "%lld %d AVE %s: %s:%d %s | fail to create CFDict %p %lld 0x%x %d"
+ "%lld %d AVE %s: %s:%d %s | fail to create CFDict %p %lld 0x%x %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to create property dictionary %p %lld %d"
+ "%lld %d AVE %s: %s:%d %s | fail to create property dictionary %p %lld %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to make MCTF Property dictionary %p %lld %p %d 0x%x %d"
+ "%lld %d AVE %s: %s:%d %s | fail to make MCTF Property dictionary %p %lld %p %d 0x%x %d\n"
+ "%lld %d AVE %s: %s:%d property dictionary reference count %p %lld %d"
+ "%lld %d AVE %s: %s:%d property dictionary reference count %p %lld %d\n"
+ "%lld %d AVE %s: Insufficient size for userQPMap, %d, %d"
+ "%lld %d AVE %s: Insufficient size for userQPMap, %d, %d\n"
+ "00:40:19"
+ "904.58.0"
+ "AVE_Session_MCTF_CreatePropertyDict"
+ "Jul 15 2025"
+ "psMVCostBuffer != __null"
- "%lld %d AVE %s: %s Exit %p %p %lld %d"
- "%lld %d AVE %s: %s Exit %p %p %lld %d\n"
- "%lld %d AVE %s: %s:%d %s | fail to create CFDict %p %lld %p %d"
- "%lld %d AVE %s: %s:%d %s | fail to create CFDict %p %lld %p %d\n"
- "%lld %d AVE %s: %s:%d %s | fail to create MCTF Propery Dict %p %lld %p %d %d %p %d"
- "%lld %d AVE %s: %s:%d %s | fail to create MCTF Propery Dict %p %lld %p %d %d %p %d\n"
- "23:03:36"
- "904.33.0"
- "AVE_DevCap.cpp"
- "AVE_DevCap_Find"
- "AVE_DevCap_Type2Idx"
- "AVE_Prop.cpp"
- "Jun 30 2025"
- "idx >= 0"
- "pDevCap != __null && pDevCap->psCEntry != __null"
- "pEntry->Add != __null"
- "pMCTF->pPropDict != __null"

```
