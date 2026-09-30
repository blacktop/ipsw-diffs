## BTAudioHALPlugin

> `/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/Contents/MacOS/BTAudioHALPlugin`

```diff

-  __TEXT.__text: 0x92588
+  __TEXT.__text: 0x92a8c
   __TEXT.__auth_stubs: 0x1210
   __TEXT.__objc_stubs: 0x1f00
   __TEXT.__init_offsets: 0xb4

   __TEXT.__gcc_except_tab: 0x27e0
   __TEXT.__const: 0x1cbc
   __TEXT.__cstring: 0x539b
-  __TEXT.__oslogstring: 0x1987f
+  __TEXT.__oslogstring: 0x19b18
   __TEXT.__objc_methname: 0x2956
   __TEXT.__objc_classname: 0x112
   __TEXT.__objc_methtype: 0x7b4
   __TEXT.__unwind_info: 0x2060
   __TEXT.__eh_frame: 0x50
-  __DATA_CONST.__const: 0x7970
+  __DATA_CONST.__const: 0x79d8
   __DATA_CONST.__cfstring: 0x1780
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3270
+  Functions: 3273
   Symbols:   424
-  CStrings:  3246
+  CStrings:  3254
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA.__bss : content changed
CStrings:
+ "HostGrid Anchor c:%llu,len:%u,Q:%f~%u,curr:%f,bufSize:%u,Seq:%x"
+ "HostGrid NoReset adj: %f,prevHostT:%llu,currHostT:%llu,gap:%f,origST:%f,adjusted sample time:%f,SampleRate:%f,bufSize:%u"
+ "HostGrid NoReset roundup: currST:%f -> %f, diff:%f, 5ms:%f, bufSize:%u"
+ "HostGrid NoReset: invalid frontline host time (frontLine:%llu, current:%llu, bufSize:%u), skipping gap adjustment"
+ "HostGrid Reset skipped: StartIO while eSCO disconnect pending"
+ "HostGrid jumped back c:%llu,Q:%f~%u,curr:%f,ATs:%f,bufSize:%u"
+ "HostGrid reA drop:%f >= bufSize:%u, forcing re-anchor; prevATs:%f,prevQ:%f~%u,curr:%f,ATs:%f"
+ "HostGrid reA prevATs:%f,prevQ:%f~%u,drop:%f,Q:%f~%u,curr:%f,ATs:%f,bufSize:%u,Seq:%u , @ %llu"
+ "HostGrid should not come here c:%llu,Q:%f~%u,curr:%f,ATs:%f,bufSize:%u"
+ "Hostgrid HasPendingHAoSDisconnect: %{public}s"
+ "Hostgrid HasPendingHAoSDisconnect: fresh to HAoS, nopending disconnect"
+ "hostgrid SetCodecChangedToHAoS: %{public}s"
- "HostGrid Anchor c:%llu,len:%u,Q:%f~%u,curr:%f,Seq:%x"
- "HostGrid jumped back c:%llu,Q:%f~%u,curr:%f,ATs:%f"
- "HostGrid reA prevATs:%f,prevQ:%f~%u,drop:%f,Q:%f~%u,curr:%f,ATs:%f,Seq:%u , @ %llu"
- "HostGrid should not come here c:%llu,Q:%f~%u,curr:%f,ATs:%f"

```
