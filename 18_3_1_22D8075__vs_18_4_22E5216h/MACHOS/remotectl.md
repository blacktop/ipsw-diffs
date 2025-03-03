## remotectl

> `/usr/libexec/remotectl`

```diff

-172.80.4.0.0
-  __TEXT.__text: 0x1ad78
-  __TEXT.__auth_stubs: 0x1aa0
+172.100.9.0.0
+  __TEXT.__text: 0x1a214
+  __TEXT.__auth_stubs: 0x1a40
   __TEXT.__objc_stubs: 0xc0
-  __TEXT.__const: 0x63c
-  __TEXT.__gcc_except_tab: 0x2b8
-  __TEXT.__cstring: 0x23c7
+  __TEXT.__objc_methlist: 0x104
+  __TEXT.__const: 0x7be
+  __TEXT.__gcc_except_tab: 0x2b4
+  __TEXT.__cstring: 0x2024
   __TEXT.__objc_classname: 0x35
   __TEXT.__oslogstring: 0x12c4
   __TEXT.__objc_methname: 0x2c8

   __TEXT.__swift5_mpenum: 0x34
   __TEXT.__swift5_capture: 0x10
   __TEXT.__objc_methtype: 0xad
-  __TEXT.__unwind_info: 0x560
+  __TEXT.__unwind_info: 0x518
   __TEXT.__eh_frame: 0x73c
-  __DATA_CONST.__auth_got: 0xd60
+  __DATA_CONST.__auth_got: 0xd30
   __DATA_CONST.__got: 0x260
   __DATA_CONST.__auth_ptr: 0x218
-  __DATA_CONST.__const: 0x6f0
+  __DATA_CONST.__const: 0x6e0
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA.__objc_const: 0x7c8
-  __DATA.__objc_selrefs: 0xa0
+  __DATA.__objc_const: 0x5d8
+  __DATA.__objc_selrefs: 0x140
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x6a0
   __DATA.__bss: 0x810

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 392
+  Functions: 366
   Symbols:   571
-  CStrings:  462
+  CStrings:  441
 
Symbols:
+ _objc_retain_x23
+ _objc_retain_x27
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _$sSs8UTF8ViewVys5UInt8VSS5IndexVcig
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _objc_release_x28
- _objc_retain_x26
- _objc_retain_x28
CStrings:
+ "assertion failure: \"cmd_argv_copy != ((void*)0)\" -> %llu"
+ "assertion failure: \"errSecSuccess == SecIdentityCopyCertificate(identity, &idCert)\" -> %llu"
+ "assertion failure: \"errSecSuccess == SecIdentityCopyPrivateKey(identity, &idKey)\" -> %llu"
+ "assertion failure: \"idPubKey = SecKeyCopyPublicKey(idKey)\" -> %llu"
+ "assertion failure: \"idPubKeyData = (__bridge_transfer NSData *)SecKeyCopyExternalRepresentation(idPubKey, ((void*)0))\" -> %llu"
+ "assertion failure: \"local_services != ((void*)0) && xpc_get_type(local_services) == (&_xpc_type_array)\" -> %llu"
+ "assertion failure: \"posix_spawn_file_actions_adddup2(&filact, null_fd, 0)\" -> %llu"
+ "assertion failure: \"posix_spawn_file_actions_adddup2(&filact, null_fd, 1)\" -> %llu"
+ "assertion failure: \"posix_spawn_file_actions_adddup2(&filact, null_fd, 2)\" -> %llu"
+ "assertion failure: \"posix_spawn_file_actions_adddup2(&filact, sock, 0)\" -> %llu"
+ "assertion failure: \"posix_spawn_file_actions_adddup2(&filact, sock, 1)\" -> %llu"
+ "assertion failure: \"posix_spawn_file_actions_adddup2(&filact, sock, passfd)\" -> %llu"
+ "assertion failure: \"posix_spawn_file_actions_addinherit_np(&filact, fds_to_inherit[i])\" -> %llu"
+ "assertion failure: \"posix_spawn_file_actions_init(&filact)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_init(&spawnattr)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_setflags(&spawnattr, 0x0002)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_setflags(&spawnattr, 0x0004 | 0x0008)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_setflags(&spawnattr, 0x4000)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_setsigdefault(&spawnattr, &all_signals)\" -> %llu"
+ "assertion failure: \"posix_spawnattr_setsigmask(&spawnattr, &no_signals)\" -> %llu"
+ "assertion failure: \"services != ((void*)0) && xpc_get_type(services) == (&_xpc_type_array)\" -> %llu"
- "--"
- "Can't construct Array with count < 0"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
- "Not enough bits to represent the passed value"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.copyMemory with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "assertion failure: \"cmd_argv_copy != ((void *)0)\" -> %lld"
- "assertion failure: \"errSecSuccess == SecIdentityCopyCertificate(identity, &idCert)\" -> %lld"
- "assertion failure: \"errSecSuccess == SecIdentityCopyPrivateKey(identity, &idKey)\" -> %lld"
- "assertion failure: \"idPubKey = SecKeyCopyPublicKey(idKey)\" -> %lld"
- "assertion failure: \"idPubKeyData = (__bridge_transfer NSData *)SecKeyCopyExternalRepresentation(idPubKey, ((void *)0))\" -> %lld"
- "assertion failure: \"local_services != ((void *)0) && xpc_get_type(local_services) == (&_xpc_type_array)\" -> %lld"
- "assertion failure: \"posix_spawn_file_actions_adddup2(&filact, null_fd, 0)\" -> %lld"
- "assertion failure: \"posix_spawn_file_actions_adddup2(&filact, null_fd, 1)\" -> %lld"
- "assertion failure: \"posix_spawn_file_actions_adddup2(&filact, null_fd, 2)\" -> %lld"
- "assertion failure: \"posix_spawn_file_actions_adddup2(&filact, sock, 0)\" -> %lld"
- "assertion failure: \"posix_spawn_file_actions_adddup2(&filact, sock, 1)\" -> %lld"
- "assertion failure: \"posix_spawn_file_actions_adddup2(&filact, sock, passfd)\" -> %lld"
- "assertion failure: \"posix_spawn_file_actions_addinherit_np(&filact, fds_to_inherit[i])\" -> %lld"
- "assertion failure: \"posix_spawn_file_actions_init(&filact)\" -> %lld"
- "assertion failure: \"posix_spawnattr_init(&spawnattr)\" -> %lld"
- "assertion failure: \"posix_spawnattr_setflags(&spawnattr, 0x0002)\" -> %lld"
- "assertion failure: \"posix_spawnattr_setflags(&spawnattr, 0x0004 | 0x0008)\" -> %lld"
- "assertion failure: \"posix_spawnattr_setflags(&spawnattr, 0x4000)\" -> %lld"
- "assertion failure: \"posix_spawnattr_setsigdefault(&spawnattr, &all_signals)\" -> %lld"
- "assertion failure: \"posix_spawnattr_setsigmask(&spawnattr, &no_signals)\" -> %lld"
- "assertion failure: \"services != ((void *)0) && xpc_get_type(services) == (&_xpc_type_array)\" -> %lld"
- "invalid Collection: less than 'count' elements in collection"

```
