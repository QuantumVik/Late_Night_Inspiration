from Late_Night_Inspiration.app.db.session import get_db_connection



class IdeaService:

    def add_idea(self,idea_data):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('INSERT INTO ideas (content) VALUES (%s)',(idea_data.content,))
        conn.commit()
        conn.close()
        c.close()
        return {'message':'Your idea successfully saved'}

    def get_ideas(self):
        conn = get_db_connection()
        c= conn.cursor()
        c.execute('SELECT * FROM ideas')
        ideas = c.fetchall()
        c.close()
        conn.close()
        idea_list=[]
        for rows in ideas:
            idea_dict = {
                'id':rows[0],
                'content':rows[1],
                'searched':rows[2],
                'clarification':rows[3]
            }
            idea_list.append(idea_dict)

        if not idea_list:
            return {'error':'No ideas are present'}
        return idea_list


    def update_idea(self,id:int,content_or_clarification):
        idea_content = content_or_clarification.content
        clarification = content_or_clarification.clarification

        if clarification or idea_content:
            conn = get_db_connection()
            c= conn.cursor()
            query = 'UPDATE ideas SET'
            value = []
            if clarification:
                query  +='clarification =%s'
                value.append(clarification)
            if idea_content:
                query+='content =%s'
                value.append(idea_content)

            query.rstrip(', ')
            query += 'Where id =%s'
            value.append(id)

            c.execute(query,value)
            conn.commit()
            conn.close()
            c.close()
            return {'message':'Idea updated Successfully'}

        else:
            return {'error':'No clarification pr idea was given'}


    def marked_as_searched(self,id:int):
        conn = get_db_connection()
        c= conn.cursor()
        c.execute('UPDATE ideas SET searched = 1 WHERE id=%s',(id,))
        conn.close()
        c.close()
        if c.rowcount==0:
            return {"error":'No idea was found'}
        return {'message':'Idea marked as searched'}


    def add_clarification(self,id:int,clarification):
        if not clarification or len(clarification)<20:
            return {"error":'No clarification is provided'}
        conn= get_db_connection()
        c =conn.cursor()
        c.execute('UPDATE ideas SET clarification =%s WHERE id=%s',(clarification,id))

        result = self.marked_as_searched(id)# use self to refer to the method within the class

        if c.rowcount==0:
            return  {'error':'Idea not found'}
        return {'message':'Clarification is added successfully','searched_status':result}

    def get_unsearched_ideas(self):
        conn =get_db_connection()
        c =conn.cursor()
        c.execute('SELECT id,content FROM ideas WHERE searched=0')
        unsearched_ideas=c.fetchall()

        return unsearched_ideas


    # @staticmethod
    def delete_idea(self,id:int):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('DELETE FROM ideas WHERE id=%s',(id,))
        c.commit()
        c.close()
        conn.close()
        if c.rowcount==0:
            return {'error':'Idea not found'}
        return {'message':'Idea was successfully deleted'}


