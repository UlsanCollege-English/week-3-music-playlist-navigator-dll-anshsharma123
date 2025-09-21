# /src/playlist.py

class _DNode:
    __slots__ = ("title", "prev", "next")

    def __init__(self, title):
        self.title = title
        self.prev = None
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def _append_node(self, node: _DNode):
        """Helper: append node at the end."""
        if not self.head:  # empty list
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def add_song(self, title):
        """Append a song at the end."""
        node = _DNode(title)
        self._append_node(node)

    def play_first(self):
        """Start from the first song."""
        if not self.head:
            self.current = None
            return None
        self.current = self.head
        return self.current.title

    def next(self):
        """Move to the next song if possible."""
        if not self.current or not self.current.next:
            return None
        self.current = self.current.next
        return self.current.title

    def prev(self):
        """Move to the previous song if possible."""
        if not self.current or not self.current.prev:
            return None
        self.current = self.current.prev
        return self.current.title

    def insert_after_current(self, title):
        """Insert new song after the current one."""
        if not self.current:
            # if no current, just add to the end
            self.add_song(title)
            return

        new_node = _DNode(title)
        nxt = self.current.next
        # link new_node
        new_node.prev = self.current
        new_node.next = nxt
        self.current.next = new_node
        if nxt:
            nxt.prev = new_node
        else:
            # current was tail
            self.tail = new_node

    def remove_current(self):
        """Remove the current song and move cursor."""
        if not self.current:
            return False

        prev_node = self.current.prev
        next_node = self.current.next

        # fix head and tail
        if self.current == self.head:
            self.head = next_node
        if self.current == self.tail:
            self.tail = prev_node

        # unlink
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node

        # move current
        if next_node:
            self.current = next_node
        elif prev_node:
            self.current = prev_node
        else:
            self.current = None  # list is empty

        return True

    def to_list(self):
        """Return playlist as a list of titles."""
        result = []
        node = self.head
        while node:
            result.append(node.title)
            node = node.next
        return result
