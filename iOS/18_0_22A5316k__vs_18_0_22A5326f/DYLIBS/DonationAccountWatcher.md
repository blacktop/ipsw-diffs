## DonationAccountWatcher

> `/System/Library/Accounts/Notification/DonationAccountWatcher.bundle/DonationAccountWatcher`

```diff

   __TEXT.__objc_methname: 0x483
   __TEXT.__objc_methtype: 0x261
   __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0x48
+  __DATA_CONST.__const: 0x88
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 92
-  Symbols:   70
-  CStrings:  49
+  Symbols:   78
+  CStrings:  8
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "\x9a[\x01\xc0\xe1j\xe8\xfb\x9a[\x01\xc0\xe1j\b\xfc\x9a[\x01\xc0\xe1j(\xfc\x9a[\x01\xc0\xe1jH\xfc\x9a[\x01\xc0\xe1jh\xfc\x9a[\x01\xc0\xe1j\x88\xfc\x9a[\x01\xc0\xe1j\xa8\xfc\x9a[\x01\xc0\xe1j\xc8\xfc\x9a[\x01\xc0\xe1j\xe8\xfc\x9a[\x01\xc0\xe1j\b\xfd\x9a[\x01\xc0\xe1j(\xfd\x9a[\x01\xc0\xe1jH\xfd\x9a[\x01\xc0\xe1jh\xfd\x9a[\x01\xc0\xe1j\x88\xfd\x9a[\x01\xc0\xe1j\xa8\xfd\x9a[\x01\xc0\xe1j\xc8\xfd\x9a[\x01\xc0\xe1j\xe8\xfd\x9a[\x01\xc0\xe1j\b\xfe\x9a[\x01\xc0\xe1j(\xfe\x9a[\x01\xc0\xe1jH\xfe\x9a[\x01\xc0\xe1jh\xfe\x9a[\x01\xc0\xe1j\x88\xfe\x9a[\x01\xc0\xe1j\xa8\xfe\x9a[\x01\xc0\xe1j\xc8\xfe\x9a[\x01\xc0\xe1j\xe8\xfe\x9a[\x01\xc0\xe1j\b\xff\x9a[\x01\xc0\xe1j(\xff\x9a[\x01\xc0\xe1jH\xff\x9a[\x01\xc0\xe1jh\xff\x9a[\x01\xc0\xe1j\x88\xff\x9a[\x01\xc0\xe1j\xa8\xff\x9a[\x01\xc0\xe1j\xc8\xff\x9a[\x01\xc0\xe1j\xe8\xff\x9a[\x01\xc0\xe1j\b"
+ "\x9b[\x01\xc0\xe1j("
+ "\x9b[\x01\xc0\xe1jH"
+ "\x9b[\x01\xc0\xe1jh"
+ "\x9b[\x01\xc0\xe1j\x88"
+ "\x9b[\x01\xc0\xe1j\xa8"
+ "\x9b[\x01\xc0\xe1j\xc8"
+ "\x9b[\x01\xc0\xe1j\xe8"
- "0_"
- "__ZN4llvm10ThreadPool4growEi"
- "__ZN4llvm10TimeRecord14getCurrentTimeEb"
- "__ZN4llvm10hash_valueENS_9StringRefE"
- "__ZN4llvm12DenseMapInfoINS_9StringRefEvE12getHashValueES1_"
- "__ZN4llvm12RISCVISAInfo13parseFeaturesEjRKNSt3__16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE"
- "__ZN4llvm12RISCVISAInfo27isSupportedExtensionFeatureENS_9StringRefE"
- "__ZN4llvm13getNamedTimerENS_9StringRefES0_"
- "__ZN4llvm16NamedRegionTimerC1ENS_9StringRefES1_S1_S1_b"
- "__ZN4llvm18getAsSignedIntegerENS_9StringRefEjRx"
- "__ZN4llvm19SmallPtrSetImplBase14insert_imp_bigEPKv"
- "__ZN4llvm19SmallPtrSetImplBase16shrink_and_clearEv"
- "__ZN4llvm20getAsUnsignedIntegerENS_9StringRefEjRy"
- "__ZN4llvm22consumeUnsignedIntegerERNS_9StringRefEjRy"
- "__ZN4llvm22timeTraceProfilerBeginENS_9StringRefENS_12function_refIFNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEvEEE"
- "__ZN4llvm22timeTraceProfilerBeginENS_9StringRefES0_"
- "__ZN4llvm28getTimeTraceProfilerInstanceEv"
- "__ZN4llvm4SHA16resultEv"
- "__ZN4llvm5RISCV12parseCPUKindENS_9StringRefE"
- "__ZN4llvm5RISCV16parseTuneCPUKindENS_9StringRefEb"
- "__ZN4llvm5RISCV20fillValidCPUArchListERNS_15SmallVectorImplINS_9StringRefEEEb"
- "__ZN4llvm5RISCV24fillValidTuneCPUArchListERNS_15SmallVectorImplINS_9StringRefEEEb"
- "__ZN4llvm5Timer5clearEv"
- "__ZN4llvm5TimerD1Ev"
- "__ZN4llvm6AMDGPU15getArchNameR600ENS0_7GPUKindE"
- "__ZN4llvm6AMDGPU17getArchNameAMDGCNENS0_7GPUKindE"
- "__ZN4llvm6AMDGPU21fillValidArchListR600ERNS_15SmallVectorImplINS_9StringRefEEE"
- "__ZN4llvm6AMDGPU23fillValidArchListAMDGCNERNS_15SmallVectorImplINS_9StringRefEEE"
- "__ZN4llvm6SHA2564hashENS_8ArrayRefIhEE"
- "__ZN4llvm6SHA2565finalEv"
- "__ZN4llvm6SHA2566updateENS_9StringRefE"
- "__ZN4llvm6SHA256C2Ev"
- "__ZN4llvm6SHA256D2Ev"
- "__ZN4llvm6SHA256aSERKS0_"
- "__ZN4llvm6Triple13getOSTypeNameENS0_6OSTypeE"
- "__ZN4llvm6TripleC1ERKNS_5TwineE"
- "__ZNK4llvm12RISCVISAInfo12hasExtensionENS_9StringRefE"
- "__ZNK4llvm12RISCVISAInfo15toFeatureVectorEv"
- "__ZNK4llvm9StringRef12find_last_ofES0_m"
- "__ZNK4llvm9StringRef12getAsIntegerEjRNS_5APIntE"
- "__ZNK4llvm9StringRef13find_first_ofES0_m"
- "__ZNK4llvm9StringRef16find_last_not_ofES0_m"
- "__ZNK4llvm9StringRef16find_last_not_ofEcm"
- "__ZNK4llvm9StringRef17find_first_not_ofES0_m"
- "__ZNK4llvm9StringRef5splitERNS_15SmallVectorImplIS0_EES0_ib"
- "__ZNK4llvm9StringRef5splitERNS_15SmallVectorImplIS0_EEcib"
- "ef17find_first_not_ofEcm"
- "ionENS_9StringRefERNS0_22ParsedBranchProtectionERS1_"
- "llvm5Regex6escapeENS_9StringRefE"

```
