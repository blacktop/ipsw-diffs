## JavaScriptCore

> `/System/Library/Frameworks/JavaScriptCore.framework/JavaScriptCore`

```diff

-623.1.14.10.9
-  __TEXT.__text: 0x18a669c
+623.2.2.0.0
+  __TEXT.__text: 0x18a897c
   __TEXT.__jsc_int: 0x59254
   __TEXT.__auth_stubs: 0x2eb0
   __TEXT.__objc_methlist: 0xb9c
   __TEXT.__const: 0x8cf68
   __TEXT.__dlsym_cstr: 0x34
-  __TEXT.__cstring: 0xe5493
+  __TEXT.__cstring: 0xe54e1
   __TEXT.__oslogstring: 0x9bc
   __TEXT.__gcc_except_tab: 0x2574
-  __TEXT.__unwind_info: 0x20f8
+  __TEXT.__unwind_info: 0x2100
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0xee
   __TEXT.__objc_methname: 0x1e51

   __DATA.__data: 0x648
   __DATA.__jsc_opcodes: 0x4000
   __DATA.__bss: 0x27c9
-  __DATA.__common: 0x480680
+  __DATA.__common: 0x480640
   __DATA_DIRTY.__objc_ivar: 0x8
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__data: 0x16a18
   __DATA_DIRTY.__wtf_config: 0x4000
   __DATA_DIRTY.__common: 0x4fbc
-  __DATA_DIRTY.__bss: 0x3331
+  __DATA_DIRTY.__bss: 0x3371
   - /System/Library/Frameworks/BrowserEngineCore.framework/BrowserEngineCore
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B5271C3A-F15A-3D46-9314-74D3F2381560
-  Functions: 39853
-  Symbols:   83898
-  CStrings:  20666
+  UUID: A6DBAEEC-BACC-36AD-ABBB-A774D9D3CF77
+  Functions: 39822
+  Symbols:   83829
+  CStrings:  20671
 
Symbols:
+ __ZN3JSC4Yarr13YarrGeneratorINS0_16YarrJITRegistersEE12generateTermEmRNS3_12MatchTargetsE
+ __ZN3JSC4Yarr13YarrGeneratorINS0_16YarrJITRegistersEE9backtrackEv
+ __ZN3WTF6VectorIN3JSC4Yarr16BoyerMooreBitmapELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEE6shrinkEm
+ __ZNSt3__117__call_once_proxyB8sn200100INS_5tupleIJOZN3JSC9VMManager9singletonEvE3$_0EEEEEvPv
- __ZGVZN3JSC9VMManager9singletonEvE7manager
- __ZN3JSC14MacroAssembler4or32ENS_22AbstractMacroAssemblerINS_15ARM64EAssemblerEE5Imm32ENS_14ARM64Registers10RegisterIDE
- __ZN3JSC4Yarr12ByteCompiler10checkInputEj
- __ZN3JSC4Yarr12ByteCompiler12uncheckInputEj
- __ZN3JSC4Yarr12ByteCompiler16haveCheckedInputEj
- __ZN3JSC4Yarr12ByteCompiler17atomBackReferenceEjNS0_14MatchDirectionEjjN3WTF7CheckedIjNS3_15CrashOnOverflowEEENS0_14QuantifierTypeENS3_9OptionSetINS0_5FlagsELNS3_14ConcurrencyTagE0EEE
- __ZN3JSC4Yarr12ByteCompiler21assertionWordBoundaryEbNS0_14MatchDirectionEjN3WTF9OptionSetINS0_5FlagsELNS3_14ConcurrencyTagE0EEE
- __ZN3JSC4Yarr12ByteCompiler25assertionDotStarEnclosureEbb
- __ZN3JSC4Yarr12ByteCompiler26atomParenthesesTerminalEndEjjN3WTF7CheckedIjNS2_15CrashOnOverflowEEES5_NS0_14QuantifierTypeE
- __ZN3JSC4Yarr12ByteCompiler28atomParenthesesTerminalBeginEjNS0_14MatchDirectionEbjjj
- __ZN3JSC4Yarr13YarrGeneratorINS0_16YarrJITRegistersEE19checkNotEnoughInputENS_14ARM64Registers10RegisterIDE
- __ZN3JSC4Yarr13YarrGeneratorINS0_16YarrJITRegistersEE21generateBackReferenceEm
- __ZN3JSC4Yarr13YarrGeneratorINS0_16YarrJITRegistersEE22backtrackBackReferenceEm
- __ZN3JSC4Yarr13YarrGeneratorINS0_16YarrJITRegistersEE24generateDotStarEnclosureEm
- __ZN3JSC4Yarr13YarrGeneratorINS0_16YarrJITRegistersEE27backtrackCharacterClassOnceEmb
- __ZN3JSC4Yarr13YarrGeneratorINS0_16YarrJITRegistersEE27generateCharacterClassFixedEm
- __ZN3JSC4Yarr13YarrGeneratorINS0_16YarrJITRegistersEE29generateAssertionWordBoundaryEm
- __ZN3JSC4Yarr13YarrGeneratorINS0_16YarrJITRegistersEE29generatePatternCharacterFixedEm
- __ZN3JSC4Yarr13YarrGeneratorINS0_16YarrJITRegistersEE31generateCharacterClassNonGreedyEm
- __ZN3JSC4Yarr13YarrGeneratorINS0_16YarrJITRegistersEE32backtrackCharacterClassNonGreedyEm
- __ZN3JSC4Yarr13YarrGeneratorINS0_16YarrJITRegistersEE33generatePatternCharacterNonGreedyEm
- __ZN3JSC4Yarr13YarrGeneratorINS0_16YarrJITRegistersEE34backtrackPatternCharacterNonGreedyEm
- __ZN3JSC4Yarr13YarrGeneratorINS0_23YarrJITDefaultRegistersEE12MatchTargets15appendSucceededENS_22AbstractMacroAssemblerINS_15ARM64EAssemblerEE4JumpE
- __ZN3JSC4Yarr13YarrGeneratorINS0_23YarrJITDefaultRegistersEE14loadSubPatternENS_14ARM64Registers10RegisterIDES5_S5_S5_
- __ZN3JSC4Yarr13YarrGeneratorINS0_23YarrJITDefaultRegistersEE21generateBackReferenceEm
- __ZN3JSC4Yarr13YarrGeneratorINS0_23YarrJITDefaultRegistersEE24generateDotStarEnclosureEm
- __ZN3JSC4Yarr13YarrGeneratorINS0_23YarrJITDefaultRegistersEE27backtrackCharacterClassOnceEmb
- __ZN3JSC4Yarr13YarrGeneratorINS0_23YarrJITDefaultRegistersEE33generatePatternCharacterNonGreedyEm
- __ZN3JSC4Yarr13YarrGeneratorINS0_23YarrJITDefaultRegistersEE34backtrackPatternCharacterNonGreedyEm
- __ZN3JSC4Yarr14BoyerMooreInfo13shortenLengthEj
- __ZN3JSC4Yarr16BoyerMooreBitmap13addCharactersENS0_8CharSizeERKN3WTF6VectorIDiLm0ENS3_15CrashOnOverflowELm16ENS3_10FastMallocEEE
- __ZN3JSC4Yarr16BoyerMooreBitmap9addRangesENS0_8CharSizeERKN3WTF6VectorINS0_14CharacterRangeELm0ENS3_15CrashOnOverflowELm16ENS3_10FastMallocEEE
- __ZN3JSC6Waiter9s_heapRefE
- __ZN3JSC9VMManager18decrementActiveVMsERNS_2VME
- __ZN3WTF6VectorIN3JSC4Yarr8ByteTermELm0ENS_15CrashOnOverflowELm16ENS_10FastMallocEE14appendSlowCaseILNS_13FailureActionE0ERS3_EEbOT0_
- __ZN3WTF6VectorIPN3JSC4Yarr13YarrGeneratorINS2_16YarrJITRegistersEE6YarrOpELm16ENS_15CrashOnOverflowELm16ENS_10FastMallocEE14appendSlowCaseILNS_13FailureActionE0ERS7_EEbOT0_
- __ZZN3JSC4Yarr13YarrGeneratorINS0_16YarrJITRegistersEE28generatePatternCharacterOnceEmRNS3_12MatchTargetsEENKUlN3WTF7CheckedIjNS6_15CrashOnOverflowEEEDitS5_E0_clES9_DitS5_
- __ZZN3JSC4Yarr13YarrGeneratorINS0_16YarrJITRegistersEE28generatePatternCharacterOnceEmRNS3_12MatchTargetsEENKUlN3WTF7CheckedIjNS6_15CrashOnOverflowEEEjjS5_E_clES9_jjS5_
- __ZZN3JSC4Yarr13YarrGeneratorINS0_16YarrJITRegistersEE28generatePatternCharacterOnceEmRNS3_12MatchTargetsEENKUlN3WTF7CheckedIjNS6_15CrashOnOverflowEEEyyyS5_E0_clES9_yyyS5_
- __ZZN3JSC9VMManager9singletonEvE7manager
CStrings:
+ "%sBackReference pattern #%u checked-offset:(%u)"
+ "%sForwardReference <not handled> checked-offset:(%u)"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/Assertions.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/Box.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/CheckedArithmetic.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/Deque.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/FastBitVector.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/HashTable.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/IndexMap.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/IntervalSet.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/JSONValues.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/LazyRef.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/LazyUniqueRef.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/Liveness.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/LockAlgorithmInlines.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/Markable.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/NaturalLoops.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/RedBlackTree.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/RefCounted.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/RefPtr.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/RobinHoodHashTable.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/SinglyLinkedListWithTail.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/WeakPtr.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
+ "/AppleInternal/Library/BuildRoots/4~CDysugB6xJxD90fZlIUZFjjQ0LJPDKnHZa0XbzU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
+ "Named"
+ "Numbered"
+ "com.apple.WebKit.WebContent.CaptivePortal"
+ "named "
+ "named forward reference"
+ "numbered "
+ "numbered forward reference"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/Assertions.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/Box.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/CheckedArithmetic.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/CheckedRef.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/ConcurrentPtrHashSet.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/Deque.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/FastBitVector.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/HashTable.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/IndexMap.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/IntervalSet.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/JSONValues.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/LazyRef.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/LazyUniqueRef.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/Liveness.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/LockAlgorithmInlines.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/Markable.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/NaturalLoops.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/RedBlackTree.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/RefCounted.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/RefPtr.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/RobinHoodHashTable.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/SinglyLinkedListWithTail.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/StdLibExtras.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/ThreadSafeWeakHashSet.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/WeakPtr.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/text/StringBuilder.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/text/StringConcatenate.h"
- "/AppleInternal/Library/BuildRoots/4~CCmyugD3F7E8oEg3O1mscTcqQd6xOiFmomTTS5E/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/wtf/text/StringImpl.h"
- "BackReference pattern #%u checked-offset:(%u)"
- "ForwardReference <not handled> checked-offset:(%u)"
- "forward reference"
- "security.mac.lockdown_mode_state"

```
