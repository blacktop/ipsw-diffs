## seputil

> `/usr/libexec/seputil`

```diff

-880.120.2.0.0
-  __TEXT.__text: 0x15a38 sha256:c72be4e5e175f9be0953570c6e1a9600fc54fbd63b01017c7011df5b5fc73b7d
-  __TEXT.__auth_stubs: 0xa80 sha256:010ffee7b16be989ee6523b58f471751de5da86f20c05b498415b80c341f903d
-  __TEXT.__cstring: 0x6364 sha256:eab25bb81b78dd5c80c15003ed0cbf127e8b060808d82e1b7df2436941fe14bc
-  __TEXT.__const: 0xc34 sha256:6088002b1323385fd6f544a57fce130de01dfd6bdb4c20f1e0aaafafb54dfda0
+926.0.0.0.0
+  __TEXT.__text: 0x16370 sha256:37736718da994e41506357e7931900e9b638d22392bc0be5ad9f7d94d8f13702
+  __TEXT.__auth_stubs: 0xa90 sha256:cd97602ee3ae9db83c03b1bfbc958fcb3a5576c520e527ba72be3a964469b9f3
+  __TEXT.__cstring: 0x65af sha256:5ce8212ce29a06cc0585675494ebca06d3b45c60e47df7c0e850962ca2b32b59
+  __TEXT.__const: 0xd14 sha256:e7ffdf1fdcdddd4fc72da857b87e9b7c2fc300b76c98b7262e33f27305ceb264
   __TEXT.__oslogstring: 0x6f sha256:b8a16caaf7fe7a19c576c0163bc1ed905e091dda7cf4ef55b06562040c88130c
-  __TEXT.__gcc_except_tab: 0x2a8 sha256:5a0cb78f8c8851124dfdf2bae49c5f611c44cd02db2d19f7fc2c08a94d11bc59
-  __TEXT.__unwind_info: 0x4d8 sha256:8c90a0b5542f2662a0850bc8e5da91cc79f8f5b971bfcce047d7bf025f7bca6d
-  __DATA_CONST.__auth_got: 0x548 sha256:981ea52b48bb5e0b770d70f9a1341eef45508bfb2f9450e059a5be19b902e8ac
-  __DATA_CONST.__got: 0xd0 sha256:beff8b912bbf63a6e2266e8361d642bc6d70647eb367b4fc114339a0e8aac500
-  __DATA_CONST.__auth_ptr: 0x18 sha256:cf7cbfd6556c986e233ac3c9a86b03599ac36d8303272070e26e92843cdd2f9b
-  __DATA_CONST.__const: 0x180 sha256:2b7f7b1f621a947be2f1b87c88449ca09b38ea6037ce32bc9dc8915809b6b841
-  __DATA_CONST.__cfstring: 0x100 sha256:3bad335696de9eede757bf0f5ebac9bdfa1d8ec369da00a12b5511e816c16602
-  __DATA.__data: 0xc80 sha256:4fde9400d24329802a9ef176ad57627d1dbb8c1871b3013426f6dd4fc821ba1c
+  __TEXT.__gcc_except_tab: 0x2a8 sha256:def2aeba31dbf2d6604e88a45637c579d0f5b3dc054cff55fcb427c9febc9e82
+  __TEXT.__unwind_info: 0x4f0 sha256:b8f7eb4cfacf77d1a1ca644865966a649f77f6e88b74eea241211c6cbf5de1de
+  __DATA_CONST.__const: 0x1e0 sha256:d807a2a89c0656d250863d3e385e05b1d54d2e7fa42ea14612c6ae0b82bcef90
+  __DATA_CONST.__cfstring: 0x120 sha256:2ff6b390bd3e25e307ed869f0c815c0c47ff3cceaf7a736bd2082b19c52b4ee0
+  __DATA_CONST.__auth_got: 0x550 sha256:163f4b047a1426c568ed8b600431faa809d2397e8f90ee930bda598daeeebdeb
+  __DATA_CONST.__got: 0xe0 sha256:4dfa979783ab1dbbc21ed53163114a1226ed67982044750d508463fba314ceda
+  __DATA_CONST.__auth_ptr: 0x18 sha256:140985eb4fed4b182fa91134629e5241b6d5a967c0afaa0add82d4a9fd6e0a1b
+  __DATA.__data: 0xc80 sha256:22c765bb993f35dbb9c3a64e1cccfbf1c951f011794bcda0c108e0c5b2af8319
   __DATA.__common: 0xc sha256:15ec7bf0b50732b49f8228e07d24365338f9e3ab994b00af08e5a3bffe55fd8b
   __DATA.__bss: 0x8f5 sha256:3b297f0ab5038205ebb7a4de94e78aeba8cd7ff6b2be85032ac747501a8763b5
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 08551A43-CEB7-315A-B2C3-4C334387A89F
-  Functions: 498
-  Symbols:   200
-  CStrings:  745
+  UUID: D38BCCE7-60EC-37F8-99E7-9704666AC8D5
+  Functions: 502
+  Symbols:   203
+  CStrings:  763
 
Symbols:
+ __NSConcreteStackBlock
+ _kIOMainPortDefault
+ _sscanf
CStrings:
+ "%2x"
+ "%s: Couldn't find property \"%s\"\n"
+ "%s: Incorrect %s entry value type\n"
+ "%s: Incorrect value size for %s property\n"
+ "%s: failed to show lynx epochs\n"
+ "%s: lynx get epochs returned 0x%x"
+ "%s: prop %s val 0x%x\n"
+ "Epoch %lu: 0x%x\n"
+ "WARNING: Chip ID 0x%x not specified as having TZ0 alignment requirements or not\n"
+ "WARNING: Unable to read chip_id, assuming SEP has TZ0 alignment requirement\n"
+ "WARNING: iBoot allocated an extremely high amount of ar0 memory!\n"
+ "WARNING: iBoot allocated an odd number of bytes for ar0 memory!\n"
+ "WARNING: iBoot did not allocate enough space for scheme2!\n"
+ "a:b:c:d:f:g:hkmno:pq:r:s:t:uv:wx:CDFQI:L:NO:PR:T:W:"
+ "chip-id"
+ "i24@?0^{?=Q{?=*Q}}8^B16"
+ "show-epochs"
+ "ucert-offset"
+ "ucert-size"
+ "ucont-offset"
+ "ucont-size"
- "\t\t--sleep                  Sleep the SEP NOW!\n"
- "%s: Sleep failed\n"
- "a:b:c:d:f:g:hkmno:pq:r:s:t:uv:wx:CDFQI:L:NO:PR:ST:W:"
- "sleep"

```
