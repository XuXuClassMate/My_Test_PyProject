import sys
import xmindparser

class TestCaseCounter:
	def __init__(self, tree):
		self.tree = tree
		self.p0_count = 0
		self.p1_count = 0
	
	def count_last_level(self, node):
		if not node.get("topics"):
			# 检查文本内容并分类统计
			title = node.get("title", "").lower()
			if "p0" in title:
				self.p0_count += 1
			elif "p1" in title:
				self.p1_count += 1
			return 1
		return sum(self.count_last_level(child) for child in node["topics"])
	
	def get_total_cases(self):
		return self.count_last_level(self.tree)
	
	def get_priority_counts(self):
		return self.p0_count, self.p1_count

def load_xmind(file_path):
	content = xmindparser.xmind_to_dict(file_path)
	# print("Parsed XMind content:", content)  # 调试信息
	return content[0]["topic"]  # 假设只有一个主节点

if __name__ == "__main__":
	if len(sys.argv) != 2:
		# print("Usage: ./testcaseSUM <xmind_file>")
		sys.exit(1)
	
	xmind_file = sys.argv[1]
	
	try:
		root_node = load_xmind(xmind_file)
		# print("Root node:", root_node)  # 调试信息
		
		counter = TestCaseCounter(root_node)
		total_cases = counter.get_total_cases()
		p0_count, p1_count = counter.get_priority_counts()
		
		print(f"测试用例总计: {total_cases} 条，其中 P0 测试用例: {p0_count} 条，P1 测试用例: {p1_count} 条")
	except Exception as e:
		print(f"Error processing the xmind file: {e}")
		sys.exit(1)
