## Migration Assistant

> `/System/Applications/Utilities/Migration Assistant.app/Contents/MacOS/Migration Assistant`

```diff

-  __TEXT.__text: 0x78b8
-  __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_stubs: 0x1e00
-  __TEXT.__objc_methlist: 0xb7c
+  __TEXT.__text: 0x7064
+  __TEXT.__auth_stubs: 0x410
+  __TEXT.__objc_stubs: 0x1d60
+  __TEXT.__objc_methlist: 0xb4c
   __TEXT.__const: 0x78
   __TEXT.__objc_classname: 0xed
-  __TEXT.__objc_methname: 0x22fa
-  __TEXT.__objc_methtype: 0x718
-  __TEXT.__cstring: 0xf9f
+  __TEXT.__objc_methname: 0x22a8
+  __TEXT.__objc_methtype: 0x710
+  __TEXT.__cstring: 0xc4c
   __TEXT.__oslogstring: 0xb
   __TEXT.__gcc_except_tab: 0x50
-  __TEXT.__unwind_info: 0x258
-  __DATA_CONST.__const: 0x2c8
-  __DATA_CONST.__cfstring: 0x1000
+  __TEXT.__unwind_info: 0x248
+  __DATA_CONST.__const: 0x298
+  __DATA_CONST.__cfstring: 0xd80
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x280
-  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__auth_got: 0x218
+  __DATA_CONST.__got: 0x1c8
   __DATA.__objc_const: 0x10b8
-  __DATA.__objc_selrefs: 0xa88
+  __DATA.__objc_selrefs: 0xa60
   __DATA.__objc_ivar: 0x94
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0xc0

   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 208
-  Symbols:   153
-  CStrings:  783
+  Functions: 200
+  Symbols:   140
+  CStrings:  731
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
- _AuthorizationExecuteWithPrivileges
- _AuthorizationRightGet
- ___error
- ___strlcpy_chk
- _chmod
- _fclose
- _fdopen
- _flock
- _fwrite
- _lstat
- _mkstemp
- _strerror
- _unlink
CStrings:
- "#! /bin/sh\nrm -f /var/db/auth.db\npkill -x authd\nrm -f \"$0\"\n"
- "(User canceled)."
- "-c"
- "."
- "/bin/sh"
- "/tmp/adbrst.XXXXXX"
- "Authorization rights: #1(%@), #2(%@)"
- "Authorization rights: Confirmed exists post reset retry."
- "Authorization rights: Confirmed exists post reset."
- "Authorization rights: Confirmed exists."
- "Authorization rights: Failed to restore rights (User canceled)."
- "Authorization rights: Failed to restore rights%@"
- "Authorization rights: Retrying Reset authDB"
- "Authorization rights: Trying Reset authDB"
- "Exists"
- "Missing"
- "Reset authDB: Cannot create a temp file [%@]"
- "Reset authDB: Cannot get a lock [%@]"
- "Reset authDB: Cannot open a temp file [%@]"
- "Reset authDB: Cannot verify that file is intact"
- "Reset authDB: Displaying user auth."
- "Reset authDB: Failed (%d)"
- "Reset authDB: Failed to create ref (%d)."
- "Reset authDB: Success"
- "authRightsExist"
- "com.apple.installassistant.requestpassword"
- "i16@0:8"
- "resetAuthDatabase"
- "right1Exists"
- "right2Exists"
- "stringWithUTF8String:"
- "w"

```
