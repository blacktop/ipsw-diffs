## libmorphun.dylib

> `/usr/lib/libmorphun.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`

```diff

-3600.35.1.0.0
+3600.36.1.0.0
   __TEXT.__text: 0x103384
   __TEXT.__const: 0x10aba0
   __TEXT.__gcc_except_tab: 0x132f0
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/agent.cc:61: std::invalid_argument: str == nullptr"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/agent.cc:69: std::invalid_argument: (ptr == nullptr) && (length != 0)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/agent.cc:84: std::logic_error: state_ != nullptr"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/io/mapper.cc:70: std::logic_error: !is_open()"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/io/mapper.cc:71: std::runtime_error: size > avail_"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/io/mapper.cc:98: std::logic_error: !is_open()"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/io/mapper.cc:99: std::runtime_error: size > avail_"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/io/writer.cc:114: std::logic_error: !is_open()"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/io/writer.cc:131: std::system_error: write: size_written <= 0"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/io/writer.cc:138: std::system_error: std::fwrite: std::fwrite(data, 1, size, file_) != size"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/io/writer.cc:140: std::system_error: std::fflush: std::fflush(file_) != 0"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/io/writer.cc:144: std::runtime_error: !stream_->write(static_cast<const char *>(data), static_cast<std::streamsize>(size))"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/io/writer.cc:145: std::runtime_error: !stream_->flush()"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/io/writer.cc:65: std::logic_error: !is_open()"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/trie/louds-trie.cc:72: std::out_of_range: agent.query().id() >= size()"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/trie/tail.cc:171: std::out_of_range: current.length() == 0"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/trie/tail.cc:193: std::length_error: buf_.size() > UINT32_MAX"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/trie/tail.cc:38: std::invalid_argument: undefined tail mode"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/keyset.cc:57: std::invalid_argument: (ptr == nullptr) && (length != 0)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/keyset.cc:58: std::invalid_argument: length > UINT32_MAX"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/trie.cc:114: std::logic_error: trie_ == nullptr"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/trie.cc:127: std::logic_error: trie_ == nullptr"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/trie.cc:147: std::logic_error: trie_ == nullptr"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/trie.cc:152: std::logic_error: trie_ == nullptr"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/trie.cc:212: std::logic_error: trie.trie_ == nullptr"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/trie.cc:39: std::invalid_argument: (ptr == nullptr) && (size != 0)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/trie.cc:90: std::logic_error: trie_ == nullptr"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9gAaQq/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/trie.cc:98: std::logic_error: trie_ == nullptr"
+ "3600.36"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/agent.cc:61: std::invalid_argument: str == nullptr"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/agent.cc:69: std::invalid_argument: (ptr == nullptr) && (length != 0)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/agent.cc:84: std::logic_error: state_ != nullptr"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/io/mapper.cc:70: std::logic_error: !is_open()"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/io/mapper.cc:71: std::runtime_error: size > avail_"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/io/mapper.cc:98: std::logic_error: !is_open()"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/io/mapper.cc:99: std::runtime_error: size > avail_"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/io/writer.cc:114: std::logic_error: !is_open()"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/io/writer.cc:131: std::system_error: write: size_written <= 0"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/io/writer.cc:138: std::system_error: std::fwrite: std::fwrite(data, 1, size, file_) != size"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/io/writer.cc:140: std::system_error: std::fflush: std::fflush(file_) != 0"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/io/writer.cc:144: std::runtime_error: !stream_->write(static_cast<const char *>(data), static_cast<std::streamsize>(size))"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/io/writer.cc:145: std::runtime_error: !stream_->flush()"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/io/writer.cc:65: std::logic_error: !is_open()"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/trie/louds-trie.cc:72: std::out_of_range: agent.query().id() >= size()"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/trie/tail.cc:171: std::out_of_range: current.length() == 0"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/trie/tail.cc:193: std::length_error: buf_.size() > UINT32_MAX"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/grimoire/trie/tail.cc:38: std::invalid_argument: undefined tail mode"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/keyset.cc:57: std::invalid_argument: (ptr == nullptr) && (length != 0)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/keyset.cc:58: std::invalid_argument: length > UINT32_MAX"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/trie.cc:114: std::logic_error: trie_ == nullptr"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/trie.cc:127: std::logic_error: trie_ == nullptr"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/trie.cc:147: std::logic_error: trie_ == nullptr"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/trie.cc:152: std::logic_error: trie_ == nullptr"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/trie.cc:212: std::logic_error: trie.trie_ == nullptr"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/trie.cc:39: std::invalid_argument: (ptr == nullptr) && (size != 0)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/trie.cc:90: std::logic_error: trie_ == nullptr"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QLG1ly/Sources/Morphun/ext/lib/Marisa/marisa-trie/lib/marisa/trie.cc:98: std::logic_error: trie_ == nullptr"
- "3600.35"
```
