## SecurityAgentHelper-arm64

> `/System/Library/Frameworks/Security.framework/Versions/A/MachServices/SecurityAgent.bundle/Contents/XPCServices/SecurityAgentHelper-arm64.xpc/Contents/MacOS/SecurityAgentHelper-arm64`

```diff

-55600.80.3.0.0
-  __TEXT.__text: 0x206e8
-  __TEXT.__auth_stubs: 0xf80
-  __TEXT.__objc_stubs: 0x4620
-  __TEXT.__objc_methlist: 0x1f1c
-  __TEXT.__const: 0x138
-  __TEXT.__objc_methname: 0x4a8e
-  __TEXT.__oslogstring: 0x2214
-  __TEXT.__objc_classname: 0x34c
+55600.80.4.0.0
+  __TEXT.__text: 0x20924
+  __TEXT.__auth_stubs: 0xfa0
+  __TEXT.__objc_stubs: 0x4640
+  __TEXT.__objc_methlist: 0x1f4c
+  __TEXT.__const: 0x140
+  __TEXT.__objc_methname: 0x4ad5
+  __TEXT.__oslogstring: 0x22bd
+  __TEXT.__objc_classname: 0x35c
   __TEXT.__objc_methtype: 0x15d8
-  __TEXT.__cstring: 0x1dc5
+  __TEXT.__cstring: 0x1e10
   __TEXT.__gcc_except_tab: 0x3c8
   __TEXT.__ustring: 0x776
   __TEXT.__dlopen_cstrs: 0x10d
-  __TEXT.__unwind_info: 0x798
+  __TEXT.__unwind_info: 0x7a0
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__auth_got: 0x7d0
+  __DATA_CONST.__auth_got: 0x7e0
   __DATA_CONST.__got: 0x410
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x820
-  __DATA_CONST.__cfstring: 0x1880
-  __DATA_CONST.__objc_classlist: 0xd8
+  __DATA_CONST.__const: 0x840
+  __DATA_CONST.__cfstring: 0x18a0
+  __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x2f70
-  __DATA.__objc_selrefs: 0x1758
+  __DATA.__objc_const: 0x3018
+  __DATA.__objc_selrefs: 0x1760
   __DATA.__objc_ivar: 0x290
-  __DATA.__objc_data: 0x870
+  __DATA.__objc_data: 0x8c0
   __DATA.__data: 0x4a0
-  __DATA.__bss: 0x158
+  __DATA.__bss: 0x168
   __DATA.__common: 0x28
   __CGPreLoginApp.__cgpreloginapp: 0x0
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A701AF3C-BD3C-3ED1-AF9D-DEB315035A35
-  Functions: 800
-  Symbols:   527
-  CStrings:  1924
+  UUID: C5D11354-9AA9-3A37-81A2-08879591B58C
+  Functions: 804
+  Symbols:   531
+  CStrings:  1933
 
Symbols:
+ _OBJC_CLASS_$_SignpostEmitter
+ _OBJC_METACLASS_$_SignpostEmitter
+ __os_signpost_emit_with_name_impl
+ _os_signpost_enabled
CStrings:
+ " enableTelemetry=YES  Notarized=%{public,signpost.telemetry:number1,name=Notarized}d  Right=%{public,signpost.telemetry:string1,name=Right}@ "
+ "PrivilegeEscalationRequest"
+ "SignpostEmitter"
+ "T@\"SignpostEmitter\",R,N"
+ "client-notarized"
+ "com.apple.ServiceManagement.blesshelper"
+ "creator-notarized"
+ "sendPrivilegeEscalationRequestNotarized:right:"

```
