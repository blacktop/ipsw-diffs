## authd

> `/System/Library/Frameworks/Security.framework/Versions/A/XPCServices/authd.xpc/Contents/MacOS/authd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-62460.1.3.0.0
-  __TEXT.__text: 0x25e98
-  __TEXT.__auth_stubs: 0x1380
+62460.40.78.0.0
+  __TEXT.__text: 0x27440
+  __TEXT.__auth_stubs: 0x1390
   __TEXT.__lazy_helpers: 0x63c
-  __TEXT.__objc_stubs: 0xc00
+  __TEXT.__objc_stubs: 0xc40
   __TEXT.__objc_methlist: 0x154
-  __TEXT.__const: 0xb10
-  __TEXT.__cstring: 0x2ea9
-  __TEXT.__oslogstring: 0x4bda
+  __TEXT.__const: 0xb20
+  __TEXT.__cstring: 0x331c
+  __TEXT.__oslogstring: 0x4f27
   __TEXT.__dlopen_cstrs: 0x5d
-  __TEXT.__gcc_except_tab: 0xd70
-  __TEXT.__objc_methname: 0x9c0
+  __TEXT.__gcc_except_tab: 0xd6c
+  __TEXT.__objc_methname: 0x9eb
   __TEXT.__objc_classname: 0xf
   __TEXT.__objc_methtype: 0x140
-  __TEXT.__unwind_info: 0x7e8
-  __DATA_CONST.__const: 0x22c8
-  __DATA_CONST.__cfstring: 0x10e0
+  __TEXT.__unwind_info: 0x818
+  __DATA_CONST.__const: 0x2528
+  __DATA_CONST.__cfstring: 0x1220
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_intobj: 0x18
+  __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x9d0
-  __DATA_CONST.__got: 0x190
+  __DATA_CONST.__auth_got: 0x9d8
+  __DATA_CONST.__got: 0x198
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x230
-  __DATA.__objc_selrefs: 0x310
+  __DATA.__objc_selrefs: 0x320
   __DATA.__objc_ivar: 0x30
   __DATA.__objc_data: 0x50
   __DATA.__lazy_load_got: 0x98

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 465
-  Symbols:   397
-  CStrings:  1046
+  Functions: 477
+  Symbols:   399
+  CStrings:  1108
 
Symbols:
+ __xpc_error_peer_code_signing_requirement
+ _xpc_connection_set_peer_code_signing_requirement
CStrings:
+ "/usr/bin/jrunscript"
+ "/usr/bin/jshell"
+ "/usr/bin/make"
+ "B32@?0@\"NSString\"8Q16^B24"
+ "DELETE FROM rules WHERE type = 1 AND name = ?"
+ "Elevation right %{public}s: outcome %{public}s, impact %d (engine %llu)"
+ "FUSAutologinDataKey"
+ "FUSDataKey"
+ "Removing right %{public}s: a case variant of a right governed by a wildcard rule"
+ "Rule %{public}s not found"
+ "SELECT * FROM rules WHERE name = ? COLLATE NOCASE ORDER BY (identifier IS NULL) DESC, id ASC LIMIT 1"
+ "SELECT COUNT(name) AS cnt FROM rules WHERE name = ? COLLATE NOCASE AND type = ?"
+ "SELECT id,name,created,identifier,requirement FROM rules WHERE name = ? COLLATE NOCASE ORDER BY (identifier IS NULL) DESC, id ASC LIMIT 1"
+ "SELECT name FROM rules WHERE type = 1 AND name GLOB '*[A-Z]*'"
+ "SELECT name FROM rules WHERE type = 1 AND name LIKE '%.'"
+ "Sheet authenticated UID %d but a different user was requested (engine %llu)"
+ "Sheet authentication denied by the smartcard policy (engine %llu)"
+ "Sheet authentication without a valid LA result (engine %llu)"
+ "Sheet authentication without the ID of the authenticated user (engine %llu)"
+ "Using local version of %{public}s"
+ "agent: peer has to satisfy %{public}s"
+ "agent: the responder does not satisfy the required code identity"
+ "agent: unable to require the peer code identity %{public}s (%d)"
+ "authorization_copy_prelogin_userdb: denying non-first-party process [%s]"
+ "clientInterpreter"
+ "com.apple.Automator"
+ "com.apple.ScriptEditor2"
+ "com.apple.ahp"
+ "com.apple.authd.elevationDialog"
+ "com.apple.bash"
+ "com.apple.csh"
+ "com.apple.dash"
+ "com.apple.expect"
+ "com.apple.ksh"
+ "com.apple.loginwindow"
+ "com.apple.make"
+ "com.apple.osacompile"
+ "com.apple.osascript"
+ "com.apple.pack200"
+ "com.apple.perl"
+ "com.apple.python3"
+ "com.apple.ruby"
+ "com.apple.sh"
+ "com.apple.shortcuts"
+ "com.apple.shortcuts.ShortcutsCommandLine"
+ "com.apple.swift-driver"
+ "com.apple.swift-frontend"
+ "com.apple.zsh"
+ "com.tcltk.tclsh"
+ "creatorInterpreter"
+ "creatorRoot"
+ "credentialOnRef"
+ "credentialShared"
+ "dialog"
+ "engine %llu: PAM service name contains invalid characters, ignoring it"
+ "engine %llu: client is not allowed to supply %{public}s, ignoring it"
+ "engine %llu: client is not entitled to select the %{public}s PAM service, ignoring it"
+ "engine %llu: running builtin sheet authenticate, setting sheet UID %d to the context"
+ "entitlement"
+ "identifier \"com.apple.SecurityAgent\" and anchor apple"
+ "identifier \"com.apple.authorizationhost\" and anchor apple"
+ "impact"
+ "indexOfObjectPassingTest:"
+ "moreRights"
+ "notGranted"
+ "otherRightName"
+ "outcome"
+ "recordedBefore"
+ "root"
+ "suppliedPassword"
+ "unknown"
+ "unsignedIntValue"
- "/usr/bin/jshell/jrunscript/usr/bin/make"
- "Credentials UID %d set."
- "Credentials UID not found for %s"
- "Rule %s not found"
- "SELECT * FROM rules WHERE name = ? LIMIT 1"
- "SELECT COUNT(name) AS cnt FROM rules WHERE name = ? AND type = 1"
- "SELECT id,created,identifier,requirement FROM rules WHERE name = ? LIMIT 1"
- "Using local version of %s"
- "engine %llu: running builtin sheet authenticate"
- "engine %llu: setting sheet UID %d to the context"
```
