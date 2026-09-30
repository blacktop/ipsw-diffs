## ssh-apple-pkcs11

> `/usr/libexec/ssh-apple-pkcs11`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-369.0.4.0.0
-  __TEXT.__text: 0x6eb84
-  __TEXT.__auth_stubs: 0x1860
+369.40.2.0.0
+  __TEXT.__text: 0x853bc
+  __TEXT.__auth_stubs: 0x1850
   __TEXT.__objc_stubs: 0x140
-  __TEXT.__const: 0x1c7e0
-  __TEXT.__cstring: 0x15d89
+  __TEXT.__const: 0x1c81c
+  __TEXT.__cstring: 0x16019
   __TEXT.__objc_methname: 0xcb
-  __TEXT.__unwind_info: 0x1170
+  __TEXT.__unwind_info: 0x1240
   __TEXT.__eh_frame: 0xa0
-  __DATA_CONST.__const: 0x22c8
+  __DATA_CONST.__const: 0x23c0
   __DATA_CONST.__cfstring: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0xc38
+  __DATA_CONST.__auth_got: 0xc30
   __DATA_CONST.__got: 0x110
   __DATA_CONST.__auth_ptr: 0x60
   __DATA.__objc_selrefs: 0x50

   - /usr/lib/libpam.2.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1097
-  Symbols:   449
-  CStrings:  3140
+  Functions: 1142
+  Symbols:   448
+  CStrings:  3167
 
Symbols:
- _ERR_load_crypto_strings
CStrings:
+ "%s: connection to %s, up %.1f seconds"
+ "(null)"
+ ".ssh/id_mldsa44_ed25519"
+ "/etc/ssh/ssh_host_mldsa44_ed25519_key"
+ "1246ACGKMNTVXYZafgknqstvxyB:D:E:F:I:J:L:O:P:Q:R:S:W:b:c:e:i:l:m:o:p:w:"
+ "COMPSIG-MLDSA44-Ed25519-SHA512"
+ "CompositeAlgorithmSignatures2025"
+ "Connection information for %s pid %lld\r\n%s  duration %s\r\n  kexalgorithm %s\r\n  hostkeyalgorithm %s\r\n  cipher %s\r\n  mac %s\r\n  compression %s\r\n  rekey %s %s\r\n  traffic %s in, %s out\r\n%s"
+ "MLDSA44-ED25519"
+ "MLDSA44-ED25519-CERT"
+ "Match directive not supported as a command-line option"
+ "OpenSSH_10.5"
+ "OpenSSH_10.5p1"
+ "X11 forwarding opened before X11 forwarding requested"
+ "bulk"
+ "channel %d: classify type \"%s\" (%s) as %s"
+ "channel_classify"
+ "channel_set_xtype"
+ "cryptographic operation failed"
+ "direct-*,forwarded-*,dynamic-*,tun-*,x11-*,session*,stdio-forward"
+ "invalid forwarding ID %d"
+ "labeled channel %d as %s (inactive timeout %u)"
+ "missing channel %d"
+ "mlkem768nistp256-sha256"
+ "multiple KEXINIT received from peer"
+ "no TTY"
+ "no-touch-required"
+ "non-transport message %u received from peer during key exchange"
+ "session:command"
+ "session:shell"
+ "session:subsystem:%s"
+ "ssh-mldsa44-ed25519-cert-v01@openssh.com"
+ "ssh-mldsa44-ed25519@openssh.com"
+ "ssh_packet_set_connection failed"
+ "usage: ssh [-46AaCfGgKkMNnqsTtVvXxYyZ] [-B bind_interface] [-b bind_address]\n           [-c cipher_spec] [-D [bind_address:]port] [-E log_file]\n           [-e escape_char] [-F configfile] [-I pkcs11] [-i identity_file]\n           [-J destination] [-L address] [-l login_name] [-m mac_spec]\n           [-O ctl_cmd] [-o option] [-P tag] [-p port] [-R address]\n           [-S ctl_path] [-W host:port] [-w local_tun[:remote_tun]]\n           destination [command [argument ...]]\n       ssh [-Q query_option]\n"
+ "verify-required"
+ "with TTY"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/OpenSSH/openssh/libcrux_mlkem768_sha3.h"
- "1246ab:c:e:fgi:kl:m:no:p:qstvxAB:CD:E:F:GI:J:KL:MNO:P:Q:R:S:TVw:W:XYy"
- "Connection information for %s pid %lld\r\n%s  kexalgorithm %s\r\n  hostkeyalgorithm %s\r\n  cipher %s\r\n  mac %s\r\n  compression %s\r\n  rekey %s %s\r\n  traffic %s in, %s out\r\n%s"
- "Connection: %s (pid %ld)"
- "OpenSSH_10.3"
- "OpenSSH_10.3p1"
- "channel_report_open"
- "direct-*,forwarded-*,tun-*,x11-*,session*"
- "unwrap_26_68"
- "usage: ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-B bind_interface] [-b bind_address]\n           [-c cipher_spec] [-D [bind_address:]port] [-E log_file]\n           [-e escape_char] [-F configfile] [-I pkcs11] [-i identity_file]\n           [-J destination] [-L address] [-l login_name] [-m mac_spec]\n           [-O ctl_cmd] [-o option] [-P tag] [-p port] [-R address]\n           [-S ctl_path] [-W host:port] [-w local_tun[:remote_tun]]\n           destination [command [argument ...]]\n       ssh [-Q query_option]\n"
```
