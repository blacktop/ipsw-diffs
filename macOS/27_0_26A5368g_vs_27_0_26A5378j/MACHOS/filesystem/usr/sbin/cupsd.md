## cupsd

> `/usr/sbin/cupsd`

```diff

-  __TEXT.__text: 0x43630
+  __TEXT.__text: 0x4358c
   __TEXT.__auth_stubs: 0x1f30
-  __TEXT.__cstring: 0x11744
-  __TEXT.__const: 0x340
-  __TEXT.__oslogstring: 0x24
-  __TEXT.__unwind_info: 0x580
+  __TEXT.__cstring: 0x118a1
+  __TEXT.__const: 0x348
+  __TEXT.__oslogstring: 0x6b
+  __TEXT.__unwind_info: 0x588
   __DATA_CONST.__const: 0xda8
   __DATA_CONST.__cfstring: 0xc0
   __DATA_CONST.__auth_got: 0xf98

   - /usr/lib/libpam.2.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 411
+  Functions: 412
   Symbols:   533
-  CStrings:  2708
+  CStrings:  2719
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
CStrings:
+ "%s: Accepting root. requesting user name=%s\n"
+ "%s: LOCAL_PEERCRED err. errno=%d\n"
+ "%s: Unauthenticated requesting user root. peer_uid=%d\n"
+ "%s: XUCRED_VERSION or size is wrong\n"
+ "Empty or NULL printer name rejected."
+ "Invalid character (0x%02x) in printer name \"%s\""
+ "Printer name too long (%zu chars, max 127): \"%s\""
+ "Unable to add printer \"%s\" - skipping entry in printers.conf"
+ "cupsdAcceptClient"
+ "cupsdIsAuthorized"
+ "cupsdIsAuthorized: using requesting-user-name=\"%s\""
+ "unauth-root"
- "cupsdIsAuthorized: requesting-user-name=\"%s\""

```
