## libccid.dylib

> `/usr/libexec/SmartCardServices/drivers/ifd-ccid.bundle/Contents/MacOS/libccid.dylib`

```diff

 55036.0.0.0.0
-  __TEXT.__text: 0x1d2e4
-  __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__const: 0x817
-  __TEXT.__cstring: 0x6bbe
-  __TEXT.__unwind_info: 0x480
+  __TEXT.__text: 0x1af50
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__const: 0x847
+  __TEXT.__cstring: 0x6ba6
+  __TEXT.__unwind_info: 0x440
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x370
+  __AUTH_CONST.__auth_got: 0x360
   __AUTH_CONST.__const: 0x128
   __AUTH_CONST.__cfstring: 0xc0
-  __AUTH_CONST.__auth_got: 0x368
+  __AUTH.__thread_vars: 0x18
+  __AUTH.__thread_bss: 0x4
   __DATA.__data: 0x1d8
-  __DATA.__thread_vars: 0x18
-  __DATA.__thread_bss: 0x4
   __DATA.__common: 0xa8
   __DATA.__bss: 0x1280
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
-  UUID: 80204241-9769-3773-827F-F73D30D76A94
-  Functions: 583
-  Symbols:   762
-  CStrings:  947
+  UUID: D9B2BE23-ED60-3C67-949C-ACF0B29A21AD
+  Functions: 386
+  Symbols:   759
+  CStrings:  940
 
Symbols:
- _T0_card_timeout
- _T1_card_timeout
- _strncmp
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SmartcardCCID/ccid/ccid/src/ccid.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SmartcardCCID/ccid/ccid/src/ccid_usb.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SmartcardCCID/ccid/ccid/src/commands.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SmartcardCCID/ccid/ccid/src/ifdhandler.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SmartcardCCID/ccid/ccid/src/openct/proto-t1.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SmartcardCCID/ccid/ccid/src/towitoko/atr.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/SmartcardCCID/ccid/ccid/src/utils.c"
+ "pthread_cond_init(cond, ((void*)0)) == 0"
+ "pthread_key_create(key, ((void*)0)) == 0"
+ "pthread_mutex_init(mutex, ((void*)0)) == 0"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SmartcardCCID/ccid/ccid/src/ccid.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SmartcardCCID/ccid/ccid/src/ccid_usb.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SmartcardCCID/ccid/ccid/src/commands.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SmartcardCCID/ccid/ccid/src/ifdhandler.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SmartcardCCID/ccid/ccid/src/openct/proto-t1.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SmartcardCCID/ccid/ccid/src/towitoko/atr.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/SmartcardCCID/ccid/ccid/src/utils.c"
- "de"
- "es"
- "fr"
- "it"
- "nl"
- "pt"
- "pthread_cond_init(cond, ((void *)0)) == 0"
- "pthread_key_create(key, ((void *)0)) == 0"
- "pthread_mutex_init(mutex, ((void *)0)) == 0"
- "tr"

```
